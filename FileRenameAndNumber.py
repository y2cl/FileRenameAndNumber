import os
import tkinter as tk
from tkinter import filedialog
import logging
import webbrowser
from datetime import date

# Create a log file with the date of creation
log_date = date.today().strftime("%Y-%m-%d")
log_file_path = f"file_renamer_{log_date}.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

def rename_files():
    try:
        # Get the input from the GUI
        name = name_entry.get()
        search_word = search_word_entry.get()
        folder_path = folder_path_entry.get()
        suffix = suffix_entry.get()
        mode = mode_var.get()

        # Check if the folder path is valid
        if not os.path.exists(folder_path):
            status_label.config(text="Invalid folder path", fg="red")
            logging.error("Invalid folder path")
            return

        # Check if the folder path is a directory
        if not os.path.isdir(folder_path):
            status_label.config(text="Invalid folder path. Please select a directory.", fg="red")
            logging.error("Invalid folder path. Please select a directory.")
            return

        # Check if the name field is empty
        if name == "" and mode == "Rename with prefix":
            status_label.config(text="Name field cannot be empty", fg="red")
            logging.error("Name field cannot be empty")
            return

        # Check if the suffix field is empty
        if suffix == "" and mode == "Add suffix":
            status_label.config(text="Suffix field cannot be empty", fg="red")
            logging.error("Suffix field cannot be empty")
            return

        # Rename all files in the folder with numbering starting with 01
        i = 1
        renamed_files = []
        for filename in os.listdir(folder_path):
            if search_word.lower() in filename.lower() or search_word == "":
                file_path = os.path.join(folder_path, filename)
                file_extension = os.path.splitext(filename)[1]
                if mode == "Rename with prefix":
                    new_filename = f"{name}_{str(i).zfill(2)}{file_extension}"
                elif mode == "Add suffix":
                    new_filename = f"{os.path.splitext(filename)[0]}-{suffix}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)

                # Check if the new file name already exists
                if os.path.exists(new_file_path):
                    # Add a number in sequence to the file name
                    base, extension = os.path.splitext(new_filename)
                    j = 1
                    while os.path.exists(new_file_path):
                        new_filename = f"{base}-{str(j).zfill(2)}{extension}"
                        new_file_path = os.path.join(folder_path, new_filename)
                        j += 1

                try:
                    os.rename(file_path, new_file_path)
                    logging.info(f"Renamed {filename} to {new_filename}")
                    status_label.config(text=f"Renamed {filename} to {new_filename}", fg="green")
                    renamed_files.append((filename, new_filename))
                except Exception as e:
                    logging.error(f"Error renaming file: {e}")
                    status_label.config(text=f"Error renaming file: {e}", fg="red")
                    continue

                i += 1

        status_label.config(text="Files renamed successfully!", fg="green")
        logging.info("Files renamed successfully!")

        # Add an option to rename more files or close the program
        rename_more_button = tk.Button(root, text="Rename more files", command=rename_more_files)
        rename_more_button.grid(row=6, column=0, padx=5, pady=5)
        undo_button = tk.Button(root, text="Undo changes", command=lambda: undo_changes(renamed_files))
        undo_button.grid(row=6, column=1, padx=5, pady=5)
        close_button = tk.Button(root, text="Close program", command=root.destroy)
        close_button.grid(row=6, column=2, padx=5, pady=5)
    except Exception as e:
        logging.error(f"Error renaming files: {e}")
        status_label.config(text=f"Error renaming files: {e}", fg="red")

def undo_changes(renamed_files):
    try:
        # Undo the changes
        for old_name, new_name in renamed_files:
            os.rename(os.path.join(folder_path_entry.get(), new_name), os.path.join(folder_path_entry.get(), old_name))
            logging.info(f"Undone change: {new_name} -> {old_name}")
            status_label.config(text=f"Undone change: {new_name} -> {old_name}", fg="green")
    except Exception as e:
        logging.error(f"Error undoing changes: {e}")
        status_label.config(text=f"Error undoing changes: {e}", fg="red")

def rename_more_files():
    try:
        # Clear the status label and remove the rename more files and close buttons
        status_label.config(text="")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button) and (widget['text'] == "Rename more files" or widget['text'] == "Close program" or widget['text'] == "Undo changes"):
                widget.destroy()

        # Clear the input fields
        name_entry.delete(0, tk.END)
        search_word_entry.delete(0, tk.END)
        folder_path_entry.delete(0, tk.END)
        suffix_entry.delete(0, tk.END)

        # Reset the mode option
        mode_var.set("Rename with prefix")

        # Add the rename button again
        rename_button = tk.Button(root, text="Rename files", command=rename_files)
        rename_button.grid(row=5, column=1, padx=5, pady=5)
    except Exception as e:
        logging.error(f"Error renaming more files: {e}")
        status_label.config(text=f"Error renaming more files: {e}", fg="red")

def browse_folder():
    try:
        # Open a file dialog to select a folder
        folder_path = filedialog.askdirectory()
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_path)
    except Exception as e:
        logging.error(f"Error browsing folder: {e}")
        status_label.config(text=f"Error browsing folder: {e}", fg="red")

def open_help_file():
    try:
        # Open the help file
        help_file_path = "help.txt"
        if os.path.exists(help_file_path):
            webbrowser.open('file://' + os.path.realpath(help_file_path))
        else:
            status_label.config(text="Help file not found", fg="red")
            logging.error("Help file not found")
    except Exception as e:
        logging.error(f"Error opening help file: {e}")
        status_label.config(text=f"Error opening help file: {e}", fg="red")

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

mode_var = tk.StringVar(root)
mode_var.set("Rename with prefix")
mode_option = tk.OptionMenu(root, mode_var, "Rename with prefix", "Add suffix")
mode_option.grid(row=3, column=1, padx=5, pady=5)
mode_label = tk.Label(root, text="Mode:")
mode_label.grid(row=3, column=0, padx=5, pady=5)

suffix_label = tk.Label(root, text="Suffix:")
suffix_label.grid(row=4, column=0, padx=5, pady=5)
suffix_entry = tk.Entry(root, width=50)
suffix_entry.grid(row=4, column=1, padx=5, pady=5)

rename_button = tk.Button(root, text="Rename files", command=rename_files)
rename_button.grid(row=5, column=1, padx=5, pady=5)

help_button = tk.Button(root, text="Help", command=open_help_file)
help_button.grid(row=6, column=3, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()


# Created by J Horsley III (2025)
# File Rename and Number ver 1.5
# Provided under GNU GPL v3 license, mofidy and use as you want.
# If you like this script, check out my comics on my website below. They are funny and will make you laugh, cry, or cringe. 
# https://y2cl.net
# https://github.com/y2cl/ljextractor
