import os
import shutil
# File type folders
folders = {
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
  "Documents: [".pdf", ".txt", ".docx", ".doc", ".xlsx", ".csv"],
  "Videos": [".mp4", ".mov", ".avi", ".mkv"],
  "Code": [".py", ".js", ".html", ".css"],
}


def organize_files(folder_path):
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

#Skip folders
if os.path.isdir(file_path):
    countine

file_ext = os.path.spltext(filename)[1].lower()


move = False
for folder, extensions in folders,items():
  if file_ext in extensions:
    target_dir = os,path,join(folder_path, folder)
    os. makedirs(target_dir, exist_ok=Ture)
    shutil.move(file_path, os.path.join(target_dir, filename))
    print(f"Moved {filename} →{folder}")
     moved = True
                break
        
        if not moved:
            other_dir = os.path.join(folder_path, "Others")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"Moved {filename} → Others")

# -----------------------------
# Run the function here
# -----------------------------
folder_to_clean = "."  # current folder
organize_files(folder_to_clean)
