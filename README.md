# File Renamer Script (Python Version)
A simple Python script that renames files in a selected folder with a custom prefix and numbered suffix.

## Description
This script allows you to select a folder and rename all files within it with a custom prefix and numbered suffix. The script also allows you to specify a word to look for in file names, so you can rename only files that contain a specific word.

## Features

* Renames files in a selected folder with a custom prefix and numbered suffix
* Allows you to specify a word to look for in file names
* Case-insensitive search
* Handles potential errors (e.g., permission issues)

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
3. Enter a word to look for in file names when prompted
4. Select the folder containing the files to rename when prompted
5. The script will rename all files in the selected folder with the specified prefix and numbered suffix

## Troubleshooting

* If you encounter any errors, check the console output for error messages
* Make sure you have the necessary permissions to rename files in the selected folder

## Contributing

Pull requests are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Known Issues

* This script does not handle subfolders. If you need to rename files in subfolders, you will need to modify the script accordingly.
* This script does not handle file name conflicts. If a file with the same name already exists, the script will overwrite it without warning.

## Future Development

* Add support for subfolders
* Add support for file name conflicts
* Improve error handling and logging
________________________________________________________________________________________________________________

##### Created by J Horsley III
[http://y2cl.net](y2cl.net)
