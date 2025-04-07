import csv
import json
from openai import OpenAI
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import logging

# Set up logging: logs will be saved to process.log
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables from .env file
load_dotenv()

model = "gemini-2.0-flash"
provider = "google"


if provider == "openai":
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

elif provider == "google":
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )    

def load_file_content(file_path):
    """
    Load and return the content of a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return ""

def load_examples(uci_example_file, general_example_files):
    """
    Load the UCI example and a list of general examples.
    Returns a tuple: (uci_example, list of general examples)
    """
    uci_example = load_file_content(uci_example_file) if uci_example_file else ""
    general_examples = []
    for file in general_example_files:
        content = load_file_content(file)
        if content:
            general_examples.append(content)
    return uci_example, general_examples

def fetch_webpage_content(url):
    """
    Fetch the content of the webpage at the given URL, then use BeautifulSoup
    to remove styling elements and inline styles, preserving the HTML structure.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove tags that are solely for styling and scripting.
        for tag in soup.find_all(["style", "script", "link", "meta"]):
            tag.decompose()
        
        # Remove inline style attributes from all tags.
        for tag in soup.find_all(True):
            if tag.has_attr("style"):
                del tag["style"]
        
        # Return the cleaned HTML as a string.
        return str(soup)
    except Exception as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return "Information not available"

def generate_json_for_dataset(name, url, uci_example, general_examples):
    """
    Generate the JSON output for a dataset given its name and URL.
    The prompt includes the UCI example, the general examples, and the filtered content of the webpage.
    The LLM output must contain two parts separated by the delimiter "====EVALUATION====":
      1. The JSON content exactly following the examples provided, with no extra text and without any markdown formatting.
      2. On a new line, output the text "====EVALUATION====" followed by the evaluation in the format "score:X; description...",
         where X is a score from 0 to 10.
    """
    joined_general_examples = "\n\n".join(general_examples)
    page_content = fetch_webpage_content(url)
    prompt = (
f"""I need a JSON file with information very similar to what is found on the UCI Machine Learning Repository.
Below are example outputs:

UCI Example:
{uci_example}

Other Examples:
{joined_general_examples}

Now, please extract the relevant information from the following webpage:
Name: "{name}"
URL: "{url}"

Below is the filtered content of the webpage:
{page_content}

You must use the webpage content above to create a JSON file that follows exactly the format of the examples provided. The webpages I provide are not always from the UCI Machine Learning Repository, so you need to read the webpage, extract the relevant information, and fill the fields accordingly. The confidence of the presented information must be high.

Keep the exact same keys used in the examples. If you do not find specific information, fill it with "Information not available". If you are not certain but it is likely, use the term "Likely".

In the "Summary", provide one or two sentences summarizing the dataset. Try to extract these sentences directly from the webpage; if not available, summarize the information you find.

For the "Description", include a longer description of 2 or 3 paragraphs. Use only the information given on the page. To break a paragraph, insert `\\n\\n`.

For the references, include the provided original reference of the dataset and any additional relevant references that you find on the webpage. Ensure that the URL and the name of the references indicate the same href element.

For "Additional Tags", create between 5 and 7 useful tags that would help someone quickly identify the dataset among many options, considering that experts in the domain will be searching for specific datasets for machine learning applications.

Your answer should consist of two parts:
1. The JSON content exactly following the examples provided, with no extra text and with no markdown formatting (do not use triple backticks or any markdown).
2. On a new line, output the text "====EVALUATION====" followed by the evaluation in the format "score:X; description...", where X is a score from 0 to 10. If you were not able to extract a large number of fields, the score should be low. If you were able to extract a large number of fields, the score should be high. The description should be a short text explaining the score.

Do not include any other text.
"""
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that returns responses in JSON format."},
            {"role": "user", "content": prompt}
        ],
    )

    generated_text = response.choices[0].message.content
    # Split the output on the delimiter
    parts = generated_text.split("====EVALUATION====")
    if len(parts) != 2:
        logging.error(f"Unexpected output format for dataset '{name}'. Full response: {generated_text}")
        return None, "No evaluation available"
    json_part = parts[0].strip()
    evaluation = parts[1].strip()

    if json_part[:7] == "```json":
        json_part=json_part[7:]
    if json_part[-3:] == "```":
        json_part=json_part[:-3]
    try:
        data = json.loads(json_part)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON for dataset '{name}': {e}")
        logging.error("JSON part was: " + json_part)
        data = None
    return data, evaluation

def main():
    input_csv = 'datasets.csv'  # CSV file with columns: Name,URL
    output_dir = 'json/llm'
    os.makedirs(output_dir, exist_ok=True)
    
    # Specify the file path for the UCI example
    uci_example_file = "json/examples/appliances_energy_prediction.json"  # Update with your UCI example file path
    
    # Specify a list of general example file paths (edit as needed)
    general_example_files = [
        "json/examples/3w.json",
        "json/examples/c_mapss_aircraft_engine_simulator_data.json",
        "json/examples/steel_industry_energy_consumption.json"
    ]
    
    uci_example, general_examples = load_examples(uci_example_file, general_example_files)

    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            url = row['URL']
            logging.info(f"Processing dataset: {name}")
            dataset_json, evaluation = generate_json_for_dataset(name, url, uci_example, general_examples)
            if dataset_json:
                safe_name = "".join([c if c.isalnum() or c in " _-" else "_" for c in name])
                filename = os.path.join(output_dir, f"{safe_name.strip().lower().replace(' ', '_')}.json")
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(dataset_json, f, indent=2)
                logging.info(f"Saved JSON for '{name}' to {filename}")
                logging.info(f"Evaluation for '{name}': {evaluation}")
            else:
                logging.error(f"Failed to generate JSON for '{name}'")

if __name__ == '__main__':
    main()
