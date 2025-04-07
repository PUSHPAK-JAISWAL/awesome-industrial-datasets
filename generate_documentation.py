import json
import os
import pandas as pd

# Define folders
json_folder_path_manual = 'json/manual'
json_folder_path_llm = 'json/llm'
md_folder_path = 'markdown'
html_folder_path = 'html/pages'
index_html_file = 'index.html'
readme_file_path = 'README.md'

os.makedirs(md_folder_path, exist_ok=True)
os.makedirs(html_folder_path, exist_ok=True)

def load_combined_json_data():
    combined_data = {}
    for folder in [json_folder_path_llm, json_folder_path_manual]:
        for filename in os.listdir(folder):
            if filename.endswith('.json') and filename.lower() not in ['template.json', 'datasets.json']:
                if filename not in combined_data or folder == json_folder_path_manual:
                    path = os.path.join(folder, filename)
                    with open(path, 'r', encoding='utf-8') as f:
                        try:
                            data = json.load(f)
                            combined_data[filename] = data
                        except Exception as e:
                            print(f"Error loading {filename}: {e}")
    return combined_data

def generate_json_index(combined_data):
    datasets = []
    for filename, data in combined_data.items():
        link_name = filename.replace('.json', '').replace(' ', '_').replace('.', '_').lower()
        datasets.append({
            "Dataset Name": data.get("Name", ""),
            "Labeled": data.get("Labeled", ""),
            "Time Series": data.get("Time Series", ""),
            "Data Source": data.get("Data Source", ""),
            "Missing Values": data.get("Missing Values", ""),
            "Dataset Characteristics": data.get("Dataset Characteristics", ""),
            "Associated Tasks": data.get("Associated Tasks", ""),
            "Number of Instances": data.get("Number of Instances", ""),
            "Number of Features": data.get("Number of Features", ""),
            "Date Donated": data.get("Date Donated", ""),
            "Summary": data.get("Summary", ""),
            "Additional Tags": "; ".join(data.get("Additional Tags", [])),
            "Link": f"html/pages/{link_name}.html"
        })
    return datasets

def inject_json_to_html(json_data, html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    script_tag = f'<script type="application/json" id="dataset-json">\n{json.dumps(json_data, indent=4)}\n</script>\n'

    if "<!-- JSON_PLACEHOLDER -->" in html_content:
        html_content = html_content.replace("<!-- JSON_PLACEHOLDER -->", script_tag)
    else:
        start_script = html_content.find('<script type="application/json" id="dataset-json">')
        if start_script != -1:
            end_script = html_content.find('</script>', start_script) + len('</script>')
            html_content = html_content[:start_script] + html_content[end_script:]
        html_content = html_content.replace("</body>", f"{script_tag}</body>")

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Injected JSON data into {html_file}")

def update_readme_with_data(combined_data, readme_file, md_folder_path):
    datasets = []
    for filename, data in combined_data.items():
        link_name = filename.replace('.json', '').replace(' ', '_').replace('.', '_').lower()
        datasets.append({
            'Dataset Name': data.get('Name', ''),
            'Labeled': data.get('Labeled', ''),
            'Dataset Characteristics': data.get('Dataset Characteristics', ''),
            'Data Source': data.get('Data Source', ''),
            'Additional Tags': '; '.join(data.get('Additional Tags', [])),
            'Description': data.get('Summary', ''),
            'Link': link_name
        })

    df = pd.DataFrame(datasets)
    df.fillna('', inplace=True)
    df.sort_values(by='Dataset Name', inplace=True)
    df['Link'] = df['Link'].apply(lambda x: f"[{x.replace('_', ' ').title()}]({md_folder_path}/{x}.md)")
    df['Dataset Name'] = df.apply(lambda x: x['Link'], axis=1)
    df.drop(['Link', 'Description'], axis=1, inplace=True)
    markdown_table = df.to_markdown(index=False)

    with open(readme_file, 'r', encoding='utf-8') as file:
        content = file.read()

    table_start = content.find("<!-- TABLE_START -->")
    table_end = content.find("<!-- TABLE_END -->")
    if table_start == -1 or table_end == -1:
        raise ValueError("Markers <!-- TABLE_START --> or <!-- TABLE_END --> not found in the README file.")

    updated_content = (
        content[:table_start] +
        "<!-- TABLE_START -->\n" +
        markdown_table +
        "\n" +
        content[table_end:]
    )

    with open(readme_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("Updated README with the new Markdown table.")

def json_to_markdown_and_html(filename, data):
    link_name = filename.replace('.json', '').replace(' ', '_').replace('.', '_').lower()
    md_path = os.path.join(md_folder_path, f"{link_name}.md")
    html_path = os.path.join(html_folder_path, f"{link_name}.html")

    # Markdown
    markdown = f"# {data['Name']}\n\n**Summary:** {data.get('Summary', '')}\n\n"
    markdown += "| Parameter | Value |\n| --- | --- |\n"
    fields = sorted(['Name', 'Labeled', 'Time Series', 'Data Source', 'Missing Values', 'Dataset Characteristics', 
                     'Feature Type', 'Associated Tasks', 'Number of Instances', 'Number of Features', 'Date Donated', 'Source'])
    for key in fields:
        if key in data:
            markdown += f"| **{key}** | {data[key]} |\n"
    markdown += "\n"

    if 'Description' in data:
        markdown += "## Description\n\n"
        for paragraph in data['Description'].split('\n\n'):
            markdown += paragraph.strip() + "\n\n"

    if 'Additional Tags' in data:
        markdown += f"## Tags\n\n{', '.join(sorted(data['Additional Tags']))}\n\n"
    if 'References' in data:
        markdown += "## References\n\n" + '\n'.join([f"- [{r['Text']}]({r['Link']})" for r in data['References']]) + "\n\n"
    markdown += "[⬅️ Back to Index](../README.md)\n"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Markdown file created for {filename}")

    # HTML
    summary_html = data.get('Summary', '').replace('\n', '<br>')
    html = f"""<html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['Name']}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="../assets/css/styles.css" rel="stylesheet"></head><body>
    <div class="container mt-5"><h1 class="mb-4">{data['Name']}</h1>
    <p>{summary_html}</p><table class="table table-striped mt-4"><tbody>"""

    for key in fields:
        if key in data:
            html += f"<tr><td><strong>{key}</strong></td><td>{data[key]}</td></tr>"
    html += "</tbody></table>"

    if 'Description' in data:
        html += "<h2>Description</h2>"
        for paragraph in data['Description'].split('\n\n'):
            html += f"<p>{paragraph.strip()}</p>"

    if 'Additional Tags' in data:
        html += "<h2>Tags</h2><ul>" + ''.join([f"<li>{t}</li>" for t in sorted(data['Additional Tags'])]) + "</ul>"
    if 'References' in data:
        html += "<h2>References</h2><ul>" + ''.join([f"<li><a href='{r['Link']}'>{r['Text']}</a></li>" for r in data['References']]) + "</ul>"

    html += """<a href="../../index.html" class="btn btn-primary mt-4">Back to Index</a></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script></body></html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML file created for {filename}")

# Main execution
combined_data = load_combined_json_data()
datasets_json = generate_json_index(combined_data)
inject_json_to_html(datasets_json, index_html_file)

for filename, data in combined_data.items():
    print(f"Processing dataset {filename}...")
    json_to_markdown_and_html(filename, data)

update_readme_with_data(combined_data, readme_file_path, md_folder_path)
