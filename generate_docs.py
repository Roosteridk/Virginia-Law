import os
import json
import re
from markdownify import markdownify as md

# Recursively add each JSON prop to the document tree
# If prop is '' skip it
# Doc id is the section number
# Each section has its own doc with

# Markdown format
# # Section Title
# Body text


keys = ["TitleNum", "TitleName", "SubtitleNum", "SubtitleName", "PartNum",
        "PartName", "ChapterNum", "ChapterName", "ArticleNum", "ArticleName",
        "SubPartNum", "SubPartName", "Section", "Title", "Body"]

sidebar = []

# Each field maps to the actual dict
dicts = dict()

def treeify(data: list[dict]):
    parent_items = sidebar
    # Iterate over each row in current level
    for row in data:
        path = "./docs/vacode"
        for i in range(0, 13, 2):

            key = keys[i]
            val: str = row[key]

            # If value is empty, skip
            if not val or not row['Section']:
                continue

            name = row[keys[i + 1]]

            content = f"# {val} {name}"
            text = f"{val} {name}"

            text_hash = str(hash(text))

            if key == "Section":
                body = row["Body"]
                section_code = val.split(" ")[1]
                try:
                    markdown = md(body)
                except:
                    print(body)
                    break
                content += f"\n\n{markdown}"

                with open(path + f"/{section_code}.md", "w") as f:
                    f.write(content)

                parent_items.append({
                    'text': text,
                    'link': f'/{section_code}'
                })
            else: 
                item = {
                    'text': text,
                    'items': []
                }

                if text_hash not in dicts.keys():
                    dicts[text_hash] = item
                    parent_items.append(item)
                
                parent_items = dicts[text_hash]['items']
            
        # short_name = re.search(r'\w+(?=Num)', key).group(0)
        # label = f"{short_name}{val}".lower()

# Read JSON files from output folder in sorted order of their titles
files = os.listdir("./output")
files.sort(key=lambda x: int(x.split(".")[0]))

for file in files:
    print(file)
    with open("./output/" + file, "r") as f:
        treeify(json.load(f))

with open("./sidebar.json", "w") as f:
    f.write(json.dumps(sidebar, ensure_ascii=False))
