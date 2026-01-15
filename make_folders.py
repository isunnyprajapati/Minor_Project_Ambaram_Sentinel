import os

folders = [
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
    "data",
    "models",
    "src",
    "templates",
]

files = [
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".env",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "src/main.py",
    "src/database.py",
    "src/processor.py",
    "src/ai_logic.py",
    "src/alerts.py",
    "check_setup.bat",
]


for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")


for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            if "README" in file:
                f.write(
                    "# ISRO MOSDAC Weather AI Project\nPrediction of extreme weather events."
                )
            pass
        print(f"Created file: {file}")

print("\n✅ Project structure is ready!")
