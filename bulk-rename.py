"""
📂 bulk_rename_files.py
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python

✨ Description:
A simple Python script to rename all files in a specified directory with a new base name,
appending an incremented number while preserving the original file extensions.

🛠️ Use Case:
Organize or standardize filenames in bulk — e.g., photos, wallpapers, documents — 
renaming files like "IMG_123.jpg" → "wallpaper1.jpg", "wallpaper2.jpg", etc.

📋 How It Works:
1️⃣ Checks if the directory exists.
2️⃣ Loops through all files inside.
3️⃣ Splits filename and extension.
4️⃣ Builds a new filename using the base name + number.
5️⃣ Renames each file.

🔑 Key Functions Used:
- os.path.isdir(): Checks directory validity.
- os.listdir(): Lists files in the directory.
- os.path.splitext(): Splits filename from extension.
- os.rename(): Renames files.
- enumerate(): Counts files to number them.

💡 For Non-Programmers:
Imagine you have many files with random names. This script renames all of them 
to a consistent format like "wallpaper1.jpg", "wallpaper2.jpg", etc., 
so your files are nicely organized.

🖥️ Example:
directory_path = "D:\\Wallpaper"
new_base_name = "wallpaper"

Running the script renames files inside D:\Wallpaper accordingly.
"""

import os

def bulk_rename_files(directory, new_name):
    # ✅ Check if directory exists
    if not os.path.isdir(directory):
        print(f"❌ The directory {directory} does not exist.")
        return

    # 🔄 Iterate through all files in directory
    for count, filename in enumerate(os.listdir(directory)):
        # 🔍 Split filename and extension
        name, ext = os.path.splitext(filename)
        
        # 🆕 Create new filename with incremented number
        new_filename = f"{new_name}{count + 1}{ext}"
        
        # 📁 Full old and new file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # 🔄 Rename the file
        os.rename(old_file, new_file)
        print(f"✅ Renamed: {old_file} ➡️ {new_file}")

# 🔧 Example usage
directory_path = "D:\\Wallpaper"  # Use double backslashes for Windows paths
new_base_name = "wallpaper"
bulk_rename_files(directory_path, new_base_name)
