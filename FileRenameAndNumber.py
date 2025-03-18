import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    # Get the input from the GUI
    name = name_entry.get()
    search_word = search_word_entry.get()
    folder_path = folder_path_entry.get()

    # Check if the folder path is valid
    if not os.path.exists(folder_path):
        status_label.config(text="Invalid folder path", fg="red")
        return

    # Rename all files in the folder with numbering starting with 01
    i = 1
    for filename in os.listdir(folder_path):
        if search_word.lower() in filename.lower() or search_word == "":
            file_path = os.path.join(folder_path, filename)
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{name}_{str(i).zfill(2)}{file_extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            i += 1

    status_label.config(text="Files renamed successfully!", fg="green")

    # Add an option to rename more files or close the program
    rename_more_button = tk.Button(root, text="Rename more files", command=rename_more_files)
    rename_more_button.grid(row=5, column=0, padx=5, pady=5)
    close_button = tk.Button(root, text="Close program", command=root.destroy)
    close_button.grid(row=5, column=2, padx=5, pady=5)

def rename_more_files():
    # Clear the status label and remove the rename more files and close buttons
    status_label.config(text="")
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and (widget['text'] == "Rename more files" or widget['text'] == "Close program"):
            widget.destroy()

    # Call the rename_files function again
    rename_files()

def browse_folder():
    # Open a file dialog to select a folder
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

root = tk.Tk()
root.title("File Renamer")

# Create the GUI elements
name_label = tk.Label(root, text="Name to change:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=5, pady=5)

search_word_label = tk.Label(root, text="Search word (optional):")
search_word_label.grid(row=1, column=0, padx=5, pady=5)
search_word_entry = tk.Entry(root, width=50)
search_word_entry.grid(row=1, column=1, padx=5, pady=5)

folder_path_label = tk.Label(root, text="Folder path:")
folder_path_label.grid(row=2, column=0, padx=5, pady=5)
folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=2, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=2, column=2, padx=5, pady=5)

rename_button = tk.Button(root, text="Rename files", command=rename_files)
rename_button.grid(row=3, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()

# Created by J Horsley III
# LiveJournal Blog Scrapper Ver. 0.3
# Provided under GNU GPL v3 license, mofidy and use as you want.
# If you like this script, check out my comics on my website below. They are funny and will make you laugh, cry, or cringe. 
# https://y2cl.net
# https://github.com/y2cl/ljextractor
