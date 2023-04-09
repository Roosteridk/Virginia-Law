import api
import os
import requests

if not os.path.exists('data'):
    os.makedirs('data')

titles = api.get_titles()

for title in titles:
    # Download corresponding title csv
    title_number = title['TitleNumber']
    print(f"Downloading title {title_number}...")
    title_csv_url = f"https://law.lis.virginia.gov/CSV/CoVTitle_{title_number}.csv"
    title_csv_response = requests.get(title_csv_url, verify=False)
    title_csv_response.encoding = 'utf-8'
    title_csv = title_csv_response.text
    with open(f"data/CoVTitle_{title_number}.csv", "w", newline='', encoding='utf-8') as f:
        f.write(title_csv)
