import os
import shutil

# Folder to organize (change path if needed)
source_folder = "test_files"

# File type mapping
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

# Create folders if not exist
for folder in file_types:
    if not os.path.exists(folder):
        os.mkdir(folder)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, folder)
                break

print("✅ Files organized successfully!")
