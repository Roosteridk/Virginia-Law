import os
import csv
import json

# Convert csv to JSON
# Create seperate file for each TitleName
# Format: TitleNum|TitleName|SubtitleNum|SubtitleName|PartNum|PartName|ChapterNum
# |ChapterName|ArticleNum|ArticleName|SubPartNum|SubPartName|Section|Title|Body
# Each column is nested in the previous column if it not empty

field_names = ["TitleNum", "TitleName", "SubtitleNum", "SubtitleName", "PartNum",
               "PartName", "ChapterNum", "ChapterName", "ArticleNum", "ArticleName",
               "SubPartNum", "SubPartName", "Section", "Title", "Body"]

if not os.path.exists('output'):
    os.makedirs('output')

for file in os.listdir("./data"):
    print("Converting " + file)
    with open("./data/" + file, "r") as f:
        reader = csv.DictReader(f, field_names, delimiter="|")
        json_data = []
        for row in reader:
            json_data.append(row)
        title = json_data[0]["TitleNum"]
        with open("./output/" + title + ".json", "w") as f:
            f.write(json.dumps(json_data, indent=4, ensure_ascii=False))
