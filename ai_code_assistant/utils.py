import os

def load_code_files(folder_path):
    code_data = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".py", ".js", ".html", ".css")):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    code_data.append((path, content))

    return code_data


def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]