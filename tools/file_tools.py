import os


OUTPUT_FOLDER = "outputs"


def save_code(filename, content):

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    filepath = os.path.join(OUTPUT_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nSaved -> {filepath}")

    return filepath