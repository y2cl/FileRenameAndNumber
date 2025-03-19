# File Renamer Script
A simple Python script that renames files in a selected folder with a custom prefix and numbered suffix.

## Description
This script allows you to select a folder and rename all files within it with a custom prefix and numbered suffix. The script also allows you to specify a word to look for in file names, so you can rename only files that contain a specific word.

## Features

* Renames files in a selected folder with a custom prefix and numbered suffix
* Allows you to specify a word to look for in file names
* Case-insensitive search
* Handles potential errors (e.g., permission issues)
* Option to rename more files or close the program after renaming
* Option to undo changes
* Log file creation with date of creation and only one log file per day
* Help file with instructions on how to use the script

## Requirements

* Python 3.x (tested on Python 3.8 and later)
* `tkinter` library (comes pre-installed with Python)
* `filedialog` library (comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/your-username/file-renamer-python.git`
2. Install the required libraries by running `pip install -r requirements.txt` (note: this script does not require any external libraries, so this step is optional)
3. Run the script by executing `python file_renamer.py`

## Usage

1. Run the script by executing `python file_renamer.py`
2. Enter a name for the files when prompted
3. Enter a word to look for in file names when prompted (optional)
4. Select the folder containing the files to rename when prompted
5. The script will rename all files in the selected folder with the specified prefix and numbered suffix
6. After renaming the files, you will have the option to rename more files or close the program

## Troubleshooting

* If you encounter any errors, check the console output for error messages
* Make sure you have the necessary permissions to rename files in the selected folder

## Updates

Here is a list of all updates since the last README was created:

* Added error handling for each button event handler to catch any exceptions that might occur when the buttons are clicked
* Updated the log file creation to include the date of creation and only one log file per day
* Added a "Help" button that opens a help file with instructions on how to use the script
* Updated the GUI to make it more readable and user-friendly
* Added an option to undo changes
* Updated the versioning to reflect the latest changes

## Versioning

This script is currently at version 1.5. Here is a breakdown of the versioning:

* Version 1.0: Initial release
* Version 1.1: Added error handling for file renaming
* Version 1.2: Added option to rename more files or close the program after renaming
* Version 1.3: Added log file creation with date of creation
* Version 1.4: Added "Help" button and updated GUI
* Version 1.5: Added option to undo changes and updated log file creation to include only one log file per day

## Contributing

Pull requests are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Known Issues

* This script does not handle subfolders. If you need to rename files in subfolders, you will need to modify the script accordingly.
* This script does not handle file name conflicts. If a file with the same name already exists, the script will overwrite it without warning.

## Requirements.txt

The `requirements.txt` file for this project is empty, as the script does not require any external libraries. However, if you want to specify the Python version required to run the script, you can add a line like this to the `requirements.txt` file:

________________________________________________________________________________________________________________

##### Created by J Horsley III
[http://y2cl.net](y2cl.net)
