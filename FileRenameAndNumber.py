import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    # Prompt for a name
    root = tk.Tk()
    root.title("File Renamer")
    label = tk.Label(root, text="Enter a name for the files:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, text="OK", command=lambda: get_name(entry.get()))
    button.pack()
    root.mainloop()

def get_name(name):
    # Prompt for a word to look for in file names
    root = tk.Tk()
    root.title("File Renamer")
    label = tk.Label(root, text="Enter a word to look for in file names:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, text="OK", command=lambda: get_word(name, entry.get()))
    button.pack()
    root.mainloop()

def get_word(name, word):
    # Select the folder containing the files to rename
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    # Rename all files in the folder with numbering starting with 01
    i = 1
    for filename in os.listdir(folder_path):
        if word.lower() in filename.lower():
            file_path = os.path.join(folder_path, filename)
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{name}_{str(i).zfill(2)}{file_extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            i += 1

    print("Files renamed successfully!")

rename_files()

# Created by J Horsley III
# File Renamne and Number Ver. 0.1
# Provided under GNU GPL v3 license, mofidy and use as you want.
# If you like this script, check out my comics on my website below. They are funny and will make you laugh, cry, or cringe. 
# https://y2cl.net
# https://github.com/y2cl/ljextractor
