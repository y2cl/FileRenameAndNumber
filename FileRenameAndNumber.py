import os
import tkinter as tk
from tkinter import filedialog, ttk
import logging
import webbrowser
from datetime import date
import csv
from datetime import datetime
import threading

# Create a log file with the date of creation
log_date = date.today().strftime("%Y-%m-%d")
log_file_path = f"file_renamer_{log_date}.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

class MainGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Renamer")

        self.label = tk.Label(self.root, text="Select an option:")
        self.label.pack()

        self.rename_button = tk.Button(self.root, text="Rename with prefix", command=self.rename_with_prefix)
        self.rename_button.pack()

        self.add_suffix_button = tk.Button(self.root, text="Add suffix", command=self.add_suffix)
        self.add_suffix_button.pack()

        self.list_files_button = tk.Button(self.root, text="List files in a folder", command=self.list_files)
        self.list_files_button.pack()

        self.close_button = tk.Button(self.root, text="Close program", command=self.root.destroy)
        self.close_button.pack()

    def rename_with_prefix(self):
        self.root.destroy()
        RenameWithPrefixGUI().run()

    def add_suffix(self):
        self.root.destroy()
        AddSuffixGUI().run()

    def list_files(self):
        self.root.destroy()
        ListFilesGUI().run()

    def run(self):
        self.root.mainloop()

class RenameWithPrefixGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rename with Prefix")

        self.name_label = tk.Label(self.root, text="Name to change:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root, width=50)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_word_label = tk.Label(self.root, text="Search word (optional):")
        self.search_word_label.grid(row=1, column=0, padx=5, pady=5)
        self.search_word_entry = tk.Entry(self.root, width=50)
        self.search_word_entry.grid(row=1, column=1, padx=5, pady=5)

        self.folder_path_label = tk.Label(self.root, text="Folder path:")
        self.folder_path_label.grid(row=2, column=0, padx=5, pady=5)
        self.folder_path_entry = tk.Entry(self.root, width=50)
        self.folder_path_entry.grid(row=2, column=1, padx=5, pady=5)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=2, column=2, padx=5, pady=5)

        self.rename_button = tk.Button(self.root, text="Rename files", command=self.rename_files)
        self.rename_button.grid(row=3, column=1, padx=5, pady=5)

        self.back_button = tk.Button(self.root, text="Back", command=self.back)
        self.back_button.grid(row=4, column=1, padx=5, pady=5)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.grid(row=5, column=1, padx=5, pady=5)

    def browse_folder(self):
        try:
            folder_path = filedialog.askdirectory()
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder_path)
        except Exception as e:
            logging.error(f"Error browsing folder: {e}")
            self.status_label.config(text=f"Error browsing folder: {e}", fg="red")

    def rename_files(self):
        try:
            name = self.name_entry.get()
            search_word = self.search_word_entry.get()
            folder_path = self.folder_path_entry.get()

            if not os.path.exists(folder_path):
                self.status_label.config(text="Invalid folder path", fg="red")
                logging.error("Invalid folder path")
                return

            if not os.path.isdir(folder_path):
                self.status_label.config(text="Invalid folder path. Please select a directory.", fg="red")
                logging.error("Invalid folder path. Please select a directory.")
                return

            if name == "":
                self.status_label.config(text="Name field cannot be empty", fg="red")
                logging.error("Name field cannot be empty")
                return

            i = 1
            renamed_files = []
            for filename in os.listdir(folder_path):
                if search_word.lower() in filename.lower() or search_word == "":
                    file_path = os.path.join(folder_path, filename)
                    file_extension = os.path.splitext(filename)[1]
                    new_filename = f"{name}_{str(i).zfill(2)}{file_extension}"
                    new_file_path = os.path.join(folder_path, new_filename)

                    if os.path.exists(new_file_path):
                        base, extension = os.path.splitext(new_filename)
                        j = 1
                        while os.path.exists(new_file_path):
                            new_filename = f"{base}-{str(j).zfill(2)}{extension}"
                            new_file_path = os.path.join(folder_path, new_filename)
                            j += 1

                    try:
                        os.rename(file_path, new_file_path)
                        logging.info(f"Renamed {filename} to {new_filename}")
                        self.status_label.config(text=f"Renamed {filename} to {new_filename}", fg="green")
                        renamed_files.append((filename, new_filename))
                    except Exception as e:
                        logging.error(f"Error renaming file: {e}")
                        self.status_label.config(text=f"Error renaming file: {e}", fg="red")
                        continue

                    i += 1

            self.status_label.config(text="Files renamed successfully!", fg="green")
            logging.info("Files renamed successfully!")

            rename_more_button = tk.Button(self.root, text="Rename more files", command=self.rename_more_files)
            rename_more_button.grid(row=6, column=0, padx=5, pady=5)
            undo_button = tk.Button(self.root, text="Undo changes", command=lambda: self.undo_changes(renamed_files))
            undo_button.grid(row=6, column=1, padx=5, pady=5)
            close_button = tk.Button(self.root, text="Close program", command=self.root.destroy)
            close_button.grid(row=6, column=2, padx=5, pady=5)
        except Exception as e:
            logging.error(f"Error renaming files: {e}")
            self.status_label.config(text=f"Error renaming files: {e}", fg="red")

    def rename_more_files(self):
        try:
            self.status_label.config(text="")
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button) and (widget['text'] == "Rename more files" or widget['text'] == "Close program" or widget['text'] == "Undo changes"):
                    widget.destroy()

            self.name_entry.delete(0, tk.END)
            self.search_word_entry.delete(0, tk.END)
            self.folder_path_entry.delete(0, tk.END)

            rename_button = tk.Button(self.root, text="Rename files", command=self.rename_files)
            rename_button.grid(row=3, column=1, padx=5, pady=5)
        except Exception as e:
            logging.error(f"Error renaming more files: {e}")
            self.status_label.config(text=f"Error renaming more files: {e}", fg="red")

    def undo_changes(self, renamed_files):
        try:
            for old_name, new_name in renamed_files:
                os.rename(os.path.join(self.folder_path_entry.get(), new_name), os.path.join(self.folder_path_entry.get(), old_name))
                logging.info(f"Undone change: {new_name} -> {old_name}")
                self.status_label.config(text=f"Undone change: {new_name} -> {old_name}", fg="green")
        except Exception as e:
            logging.error(f"Error undoing changes: {e}")
            self.status_label.config(text=f"Error undoing changes: {e}", fg="red")

    def back(self):
        self.root.destroy()
        MainGUI().run()

    def run(self):
        self.root.mainloop()

class AddSuffixGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Add Suffix")

        self.search_word_label = tk.Label(self.root, text="Search word (optional):")
        self.search_word_label.grid(row=0, column=0, padx=5, pady=5)
        self.search_word_entry = tk.Entry(self.root, width=50)
        self.search_word_entry.grid(row=0, column=1, padx=5, pady=5)

        self.folder_path_label = tk.Label(self.root, text="Folder path:")
        self.folder_path_label.grid(row=1, column=0, padx=5, pady=5)
        self.folder_path_entry = tk.Entry(self.root, width=50)
        self.folder_path_entry.grid(row=1, column=1, padx=5, pady=5)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        self.suffix_label = tk.Label(self.root, text="Suffix:")
        self.suffix_label.grid(row=2, column=0, padx=5, pady=5)
        self.suffix_entry = tk.Entry(self.root, width=50)
        self.suffix_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_suffix_button = tk.Button(self.root, text="Add suffix", command=self.add_suffix)
        self.add_suffix_button.grid(row=3, column=1, padx=5, pady=5)

        self.back_button = tk.Button(self.root, text="Back", command=self.back)
        self.back_button.grid(row=4, column=1, padx=5, pady=5)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.grid(row=5, column=1, padx=5, pady=5)

    def browse_folder(self):
        try:
            folder_path = filedialog.askdirectory()
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder_path)
        except Exception as e:
            logging.error(f"Error browsing folder: {e}")
            self.status_label.config(text=f"Error browsing folder: {e}", fg="red")

    def add_suffix(self):
        try:
            search_word = self.search_word_entry.get()
            folder_path = self.folder_path_entry.get()
            suffix = self.suffix_entry.get()

            if not os.path.exists(folder_path):
                self.status_label.config(text="Invalid folder path", fg="red")
                logging.error("Invalid folder path")
                return

            if not os.path.isdir(folder_path):
                self.status_label.config(text="Invalid folder path. Please select a directory.", fg="red")
                logging.error("Invalid folder path. Please select a directory.")
                return

            if suffix == "":
                self.status_label.config(text="Suffix field cannot be empty", fg="red")
                logging.error("Suffix field cannot be empty")
                return

            i = 1
            renamed_files = []
            for filename in os.listdir(folder_path):
                if search_word.lower() in filename.lower() or search_word == "":
                    file_path = os.path.join(folder_path, filename)
                    file_extension = os.path.splitext(filename)[1]
                    new_filename = f"{os.path.splitext(filename)[0]}-{suffix}{file_extension}"
                    new_file_path = os.path.join(folder_path, new_filename)

                    if os.path.exists(new_file_path):
                        base, extension = os.path.splitext(new_filename)
                        j = 1
                        while os.path.exists(new_file_path):
                            new_filename = f"{base}-{str(j).zfill(2)}{extension}"
                            new_file_path = os.path.join(folder_path, new_filename)
                            j += 1

                    try:
                        os.rename(file_path, new_file_path)
                        logging.info(f"Renamed {filename} to {new_filename}")
                        self.status_label.config(text=f"Renamed {filename} to {new_filename}", fg="green")
                        renamed_files.append((filename, new_filename))
                    except Exception as e:
                        logging.error(f"Error renaming file: {e}")
                        self.status_label.config(text=f"Error renaming file: {e}", fg="red")
                        continue

                    i += 1

            self.status_label.config(text="Files renamed successfully!", fg="green")
            logging.info("Files renamed successfully!")

            rename_more_button = tk.Button(self.root, text="Rename more files", command=self.rename_more_files)
            rename_more_button.grid(row=6, column=0, padx=5, pady=5)
            undo_button = tk.Button(self.root, text="Undo changes", command=lambda: self.undo_changes(renamed_files))
            undo_button.grid(row=6, column=1, padx=5, pady=5)
            close_button = tk.Button(self.root, text="Close program", command=self.root.destroy)
            close_button.grid(row=6, column=2, padx=5, pady=5)
        except Exception as e:
            logging.error(f"Error renaming files: {e}")
            self.status_label.config(text=f"Error renaming files: {e}", fg="red")

    def rename_more_files(self):
        try:
            self.status_label.config(text="")
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button) and (widget['text'] == "Rename more files" or widget['text'] == "Close program" or widget['text'] == "Undo changes"):
                    widget.destroy()

            self.search_word_entry.delete(0, tk.END)
            self.folder_path_entry.delete(0, tk.END)
            self.suffix_entry.delete(0, tk.END)

            add_suffix_button = tk.Button(self.root, text="Add suffix", command=self.add_suffix)
            add_suffix_button.grid(row=3, column=1, padx=5, pady=5)
        except Exception as e:
            logging.error(f"Error renaming more files: {e}")
            self.status_label.config(text=f"Error renaming more files: {e}", fg="red")

    def undo_changes(self, renamed_files):
        try:
            for old_name, new_name in renamed_files:
                os.rename(os.path.join(self.folder_path_entry.get(), new_name), os.path.join(self.folder_path_entry.get(), old_name))
                logging.info(f"Undone change: {new_name} -> {old_name}")
                self.status_label.config(text=f"Undone change: {new_name} -> {old_name}", fg="green")
        except Exception as e:
            logging.error(f"Error undoing changes: {e}")
            self.status_label.config(text=f"Error undoing changes: {e}", fg="red")

    def back(self):
        self.root.destroy()
        MainGUI().run()

    def run(self):
        self.root.mainloop()

class ListFilesGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("List Files")
        self.thread_running = False
        self.log_file_name = None

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        self.select_button = tk.Button(self.button_frame, text="Select Folder", command=self.select_folder_thread)
        self.select_button.pack(side=tk.LEFT, padx=10)
        self.back_button = tk.Button(self.button_frame, text="Back", command=self.back)
        self.back_button.pack(side=tk.LEFT, padx=10)
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack()
        self.include_subfolders_var = tk.BooleanVar()
        self.include_subfolders_checkbox = tk.Checkbutton(self.root, text="Include Subfolders", variable=self.include_subfolders_var)
        self.include_subfolders_checkbox.pack()

    def select_folder_thread(self):
        if not self.thread_running:
            self.thread_running = True
            self.select_button.config(state="disabled")
            self.thread = threading.Thread(target=self.select_folder)
            self.thread.start()
            self.check_thread()

    def check_thread(self):
        if self.thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.thread_running = False
            self.select_button.config(state="normal")

    def select_folder(self):
        try:
            folder_path = filedialog.askdirectory()
            if folder_path:
                self.log_file_name = None
                folder_name = os.path.basename(folder_path)
                self.log_file_name = f"{folder_name}_{datetime.now().strftime('%Y-%m-%d')}.log"
                logging.basicConfig(filename=self.log_file_name, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
                logging.info("Folder selected: %s", folder_path)
                file_info = self.get_file_info(folder_path)
                if file_info:
                    logging.info("File information collected successfully.")
                    self.save_to_csv(file_info, folder_name)
                else:
                    logging.error("No files found in the specified folder.")
                    self.status_label.config(text="No files found in the specified folder.", fg="red")
            else:
                logging.error("No folder selected.")
                self.status_label.config(text="No folder selected.", fg="red")
        except Exception as e:
            logging.error("Error: %s", e)
            self.status_label.config(text=f"Error: {e}", fg="red")

    def get_file_info(self, folder_path):
        file_info = []
        try:
            if self.include_subfolders_var.get():
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        file_name, file_extension = os.path.splitext(file)
                        file_size = os.path.getsize(file_path)
                        file_created_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                        file_last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                        file_info.append({
                            'File Path': os.path.dirname(file_path),
                            'File Name': file_name,
                            'File Extension': file_extension,
                            'File Size (bytes)': file_size,
                            'File Created Date': file_created_date,
                            'File Last Modified Date': file_last_modified_date
                        })
                        self.progress_bar['value'] = len(file_info)
                        self.root.update_idletasks()
                        logging.info("File information collected: %s", file_path)
            else:
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        file_name, file_extension = os.path.splitext(file)
                        file_size = os.path.getsize(file_path)
                        file_created_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                        file_last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                        file_info.append({
                            'File Path': folder_path,
                            'File Name': file_name,
                            'File Extension': file_extension,
                            'File Size (bytes)': file_size,
                            'File Created Date': file_created_date,
                            'File Last Modified Date': file_last_modified_date
                        })
                        self.progress_bar['value'] = len(file_info)
                        self.root.update_idletasks()
                        logging.info("File information collected: %s", file_path)
        except Exception as e:
            logging.error("Error collecting file information: %s", e)
        return file_info

    def save_to_csv(self, file_info, folder_name):
        try:
            current_date = datetime.now().strftime('%Y-%m-%d')
            csv_file_name = f"{folder_name}_{current_date}.csv"
            csv_columns = ['File Path', 'File Name', 'File Extension', 'File Size (bytes)', 'File Created Date', 'File Last Modified Date']
            with open(csv_file_name, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
                writer.writeheader()
                for file in file_info:
                    writer.writerow(file)
            logging.info("File information saved to CSV: %s", csv_file_name)
            self.status_label.config(text=f"File information saved to {csv_file_name}", fg="green")
        except Exception as e:
            logging.error("Error saving to CSV: %s", e)
            self.status_label.config(text=f"Error saving to CSV: {e}", fg="red")

    def back(self):
        self.root.destroy()
        MainGUI().run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = MainGUI()
    gui.run()


# Created by J Horsley III (2025)
# File Rename and Number ver 1.5
# Provided under GNU GPL v3 license, mofidy and use as you want.
# If you like this script, check out my comics on my website below. They are funny and will make you laugh, cry, or cringe. 
# https://y2cl.net
# https://github.com/y2cl/ljextractor
