import os
import json
import re

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


def treeify(data: list[dict]):
    labels = set()
    path = "./docs"

    root_label = ""
    # Iterate over each row in current level
    for row in data:

        if root_label != "":
            path = "./docs/" + root_label

        for i in range(0, 13, 2):
            key = keys[i]
            val: str = row[key]

            # If value is empty, skip
            if val == "":
                continue

            name = row[keys[i + 1]]

            content = f"# {val} {name}"

            if key == "Section":
                body = row["Body"]
                label = "section" + val.split(" ")[1]
                content += f"\n\n{body}"
            else:
                short_name = re.search(r'\w+(?=Num)', key).group(0)
                label = f"{short_name}{val}".lower()
                # Add label to path

            # If label already exists, skip label creation
            if label in labels:
                continue

            path += "/" + label
            # Create folder for label
            os.mkdir(path)

            # Create README.md file for label
            with open(path + "/README.md", "w") as f:
                f.write(content)

            labels.add(label)

            if i == 0:
                root_label = label


# Read JSON files from output folder in sorted order of their titles
files = os.listdir("./output")
files.sort(key=lambda x: int(x.split(".")[0]))

for file in files:
    print(file)
    with open("./output/" + file, "r") as f:
        treeify(json.load(f))
