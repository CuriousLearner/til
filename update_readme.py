# Initially taken from Lacey Williams Henschel & Simon Willison: https://github.com/simonw/til/blob/0abdc32464f1bc726abebdbc147b945d22bae7a8/update_readme.py
"Run this after build_database.py - it needs til.db"
import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()
KNOWN_ABBREVIATIONS = [
    "aws",
    "cli",
    "pdf",
    "psql",
    "ssh",
    "vim",
    "vlc",
]


def _get_transformed_topic(topic):
    transformed_topic = " ".join(topic.split("-"))
    transformed_topic = " ".join(transformed_topic.split("_"))
    if topic in KNOWN_ABBREVIATIONS:
        return transformed_topic.upper()
    return transformed_topic.title()


index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_re = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

COUNT_TEMPLATE = "<!-- count starts -->{}<!-- count ends -->"

if __name__ == "__main__":
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)
    index = ["<!-- index starts -->"]

    # Alphabetize the topics
    topics = sorted(list(by_topic.keys()))

    for topic in topics:
        index.append(f"## {_get_transformed_topic(topic)}\n")
        rows = by_topic[topic]
        rows.sort(key=lambda x: x["created"], reverse=True)
        for row in rows:
            index.append(
                "* [{title}]({url}) - {date}".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")
    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        rewritten = index_re.sub(index_txt, readme_contents)
        rewritten = count_re.sub(COUNT_TEMPLATE.format(db["til"].count), rewritten)
        readme.open("w").write(rewritten)
    else:
        print("\n".join(index))
