import os

def load_prompt(levelNum):
    filename = f"level-{levelNum}.md"

    with open('prompts/'+filename, "r", encoding="utf-8") as f:
        return f.read().strip()
