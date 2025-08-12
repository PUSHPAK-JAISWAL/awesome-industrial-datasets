import csv
import json
from openai import OpenAI
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up logging: logs will be saved to process.log
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables from .env file
load_dotenv()

# model = "gemini-2.0-flash"
# provider = "google"

model = "o4-mini-2025-04-16"
provider = "openai"

if provider == "openai":
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
elif provider == "google":
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    for tag in soup.find_all(["style", "script", "link", "meta"]):
        tag.decompose()
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]
    return str(soup).strip()

def use_selenium(url):
    logging.info(f"Using Selenium to fetch content from: {url}")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    driver.quit()
    return clean_html(page_source)

def fetch_webpage_content(url, allow_selenium=True):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        cleaned = clean_html(response.text)

        # Use Selenium for Kaggle or GitHub pages or if content is too short
        if "kaggle.com" in url or "github.com" in url or len(cleaned) < 300:
            if allow_selenium:
                return use_selenium(url)
        return cleaned
    except Exception as e:
        logging.warning(f"Primary fetch failed for {url}: {e}")
        if allow_selenium:
            try:
                return use_selenium(url)
            except Exception as se:
                logging.error(f"Selenium fetch also failed for {url}: {se}")
        return "Information not available"

def extract_score(evaluation_str):
    try:
        if "score:" in evaluation_str:
            score = evaluation_str.split("score:")[1].split(";")[0].strip()
            return int(score)
    except Exception as e:
        logging.error(f"Failed to extract score from evaluation string: {evaluation_str}")
    return 0

def load_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return ""

def load_examples(uci_example_file, general_example_files):
    uci_example = load_file_content(uci_example_file) if uci_example_file else ""
    general_examples = []
    for file in general_example_files:
        content = load_file_content(file)
        if content:
            general_examples.append(content)
    return uci_example, general_examples

def generate_json_for_dataset(name, url, uci_example, general_examples, page_content):
    joined_general_examples = "\n\n".join(general_examples)
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

Instructions:
1. Use only content present on the webpage to fill each field. Do not add any speculative or meta commentary about missing information or your uncertainty.
2. If a data field cannot be confirmed from the page, set it to "Information not available" but do not mention it in the "Description" or "Summary".
3. Do not include sentences about what is not available (e.g., avoid phrases like "While detailed metadata... is not disclosed").
4. Follow the exact keys and structure from the examples with no extra keys.

For the "Summary", provide one or two factual sentences summarizing the dataset based solely on page content.

For the "Description", include a factual, multi-paragraph narrative (2 or 3 paragraphs) drawn strictly from the page. Do not speculate or comment on missing data.

For "References", list each source with its link text and URL exactly as displayed on the page.

For "Additional Tags", generate 5 to 7 concise domain-specific tags drawn directly from page context or visible keywords.

Your answer should consist of two parts:
1. The JSON content exactly following the examples provided, with no extra text and with no markdown formatting (do not use triple backticks or any markdown).
2. On a new line, output the text "====EVALUATION====" followed by the evaluation in the format "score:X; description...", where X is a score from 0 to 10. The score is based on the number of field extracted and the precision of the information. A score of 10 means all fields were extracted with high quality and confidence, while a score of 0 means no relevant information was extracted. If 4 or more fields are filled with "Information not available", the score should be 3 or lower. The description should be a short text explaining the score.

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
    parts = generated_text.split("====EVALUATION====")
    if len(parts) != 2:
        logging.error(f"Unexpected output format for dataset '{name}'. Full response: {generated_text}")
        return None, "No evaluation available"

    json_part = parts[0].strip()
    evaluation = parts[1].strip()

    if json_part.startswith("```json"):
        json_part = json_part[7:]
    if json_part.endswith("```"):
        json_part = json_part[:-3]

    try:
        data = json.loads(json_part)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON for dataset '{name}': {e}")
        logging.error("JSON part was: " + json_part)
        data = None
    return data, evaluation

def try_generate_with_fallback(name, url, uci_example, general_examples, generate_fn):
    page_content = fetch_webpage_content(url, allow_selenium=False)
    print(page_content)
    dataset_json, evaluation = generate_fn(name, url, uci_example, general_examples, page_content)
    score = extract_score(evaluation)

    if score <= 5:
        logging.info(f"Low score ({score}) for '{name}', retrying with Selenium...")
        page_content = fetch_webpage_content(url, allow_selenium=True)
        dataset_json_retry, evaluation_retry = generate_fn(name, url, uci_example, general_examples, page_content)
        score_retry = extract_score(evaluation_retry)

        if score_retry > score:
            logging.info(f"Retry improved score from {score} to {score_retry}")
            return dataset_json_retry, evaluation_retry
        else:
            return dataset_json, evaluation
    return dataset_json, evaluation

def main():
    input_csv = 'datasets.csv'
    output_dir = 'json/llm'
    os.makedirs(output_dir, exist_ok=True)

    uci_example_file = "json/examples/appliances_energy_prediction.json"
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
            dataset_json, evaluation = try_generate_with_fallback(name, url, uci_example, general_examples, generate_json_for_dataset)
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
