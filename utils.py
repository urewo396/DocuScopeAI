import re

def clean_text(text: str) -> str:
    text = text.replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text

text = "  no siema  "

text = clean_text(text)
print(text)