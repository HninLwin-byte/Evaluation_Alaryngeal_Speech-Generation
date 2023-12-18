import shutil
import os

# Specify the paths to the source and destination folders
source_folder = '/Users/krislwin/Documents/Speech_Website/assets'
destination_folder = '/Users/krislwin/Documents/Speech_Website/copy'

# List all files in the source folder
files_to_copy = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Copy each file from the source folder to the destination folder
for file_name in files_to_copy:
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)
    
    shutil.copy2(source_path, destination_path)

print("Files have been successfully copied to the destination folder.")
