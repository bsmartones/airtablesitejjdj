import os
import requests

# Airtable Base and API Key
API_URL = "https://api.airtable.com/v0/appXXXXXXXXX/TableName"
API_KEY = "keyXXXXXXXXXXX"

headers = {"Authorization": f"Bearer {API_KEY}"}

HTML_FOLDER = "generated_html"

def get_records():
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get("records", [])
    else:
        response.raise_for_status()

def generate_html(record):
    data = record.get("fields", {})
    status = data.get("Status")
    if status != "generate":
        return
    
    html_content = f"<html><body><h1>{data.get('Title')}</h1><p>{data.get('Description')}</p></body></html>"
    file_name = os.path.join(HTML_FOLDER, f"{record['id']}.html")
    with open(file_name, "w") as file:
        file.write(html_content)
    
    print(f"Generated {file_name}")

def main():
    records = get_records()
    for record in records:
        generate_html(record)

if __name__ == "__main__":
    main()
