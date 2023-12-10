'''
CleanDesktop.py

This script is designed to clean up the desktop by moving specific types of files into a new folder labeled with the current date and time. 

Note: 
1. The script should be placed in its own folder on the desktop.
2. The script assumes the desktop folder is the parent folder of the current directory.

Files to be cleaned:
- PDF files
- Images (JPEG files)
- Text files
- PowerPoint files
- Word document files

If you want to add more file types to be cleaned, add them to the 'extensions' list below on line 38.
extensions = [".pdf", ".txt", ".jpg", ".docx", ".doc", ".pptx"]

Author: Jacob Campbell
Date: 12-10-2023
'''

# import modules

import os
import sys
import datetime
import shutil

# define variables

desktopPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
time = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
time = "CleanedDesktop" + "_" + time

# Add or remove extensions from this list to change the files to be cleaned
extenstions = [".pdf", ".txt", ".jpg", ".docx", ".doc", ".pptx"]

# Create new folder for cleaned files
os.mkdir(os.path.join(desktopPath, time))

# Loop through all files in the desktop folder, moving them into the new folder if they have appropriate extensions
counter = 0
for root, dirs, files in os.walk(desktopPath):
    print("*" * 33)
    # Only check desktop directory
    dirs.clear()
    
    for file in files:
        if file.lower().endswith(tuple(extenstions)):
            counter = counter + 1
            shutil.move(os.path.join(root, file), os.path.join(desktopPath, time, file))
            print("Moved " + file + " into " + os.path.join(desktopPath, time, file))

    print(str(counter) + " files cleaned.")
    print("*" * 33)

# if no files were moved, delete the new folder that was just created
if counter == 0:
    shutil.rmtree(os.path.join(desktopPath, time))

sys.exit(0)