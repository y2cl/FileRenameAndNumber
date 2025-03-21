# File Renamer
A simple GUI application for renaming files in a folder.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Changelog](#changelog)
7. [Versioning](#versioning)
8. [License](#license)
9. [Contributing](#contributing)

## Introduction
The File Renamer GUI is a simple application that allows users to rename files in a folder with a prefix or suffix. It also includes features to list files in a folder and save to CSV.

## Features
* Rename files in a folder with a prefix
* Add a suffix to files in a folder
* List files in a folder and save to CSV
* Error handling to prevent program from crashing if an error occurs
* Improved GUI updates to ensure progress bar and status label are updated properly

## Requirements
* Python 3.x
* Tkinter library

## Installation
1. Clone the repository using `git clone https://github.com/your-username/file-renamer-gui.git`
2. Install the required libraries using `pip install -r requirements.txt`
3. Run the application using `python main.py`

## Usage
### Rename with Prefix
1. Select a folder to rename files in
2. Enter a prefix to add to the files
3. Click the "Rename Files" button to rename the files
4. The files will be renamed with the prefix and a number (e.g. "prefix_01_file.txt")

### Add Suffix
1. Select a folder to add a suffix to files in
2. Enter a suffix to add to the files
3. Click the "Add Suffix" button to add the suffix to the files
4. The files will be renamed with the suffix (e.g. "file_suffix.txt")

### List Files
1. Select a folder to list files in
2. Click the "List Files" button to list the files in the folder
3. The files will be listed in a table with their name, size, and last modified date
4. Click the "Save to CSV" button to save the file list to a CSV file

## Changelog
### v1.0.0
* Initial release of the File Renamer GUI application
* Includes features to rename files with a prefix, add a suffix, and list files in a folder
* Error handling to prevent program from crashing if an error occurs

### v1.1.0
* Fixed issue with buttons sometimes taking several clicks to work
* Added error handling to prevent program from crashing if an error occurs while selecting a folder, collecting file information, or saving to CSV
* Improved GUI updates to ensure progress bar and status label are updated properly

### v1.2.0
* Added three new parts to the application: Rename with Prefix, Add Suffix, and List Files
* Each part has its own usage section in the README file
* Updated the changelog to reflect the addition of the three new parts

## Versioning
The File Renamer GUI application uses semantic versioning. The version number is in the format `MAJOR.MINOR.PATCH`, where:
* `MAJOR` is the major version number, which is incremented when there are significant changes to the application.
* `MINOR` is the minor version number, which is incremented when there are new features or improvements added to the application.
* `PATCH` is the patch version number, which is incremented when there are bug fixes or minor changes made to the application.

## License
The File Renamer GUI application is licensed under the MIT License.

## Contributing
Contributions to the File Renamer GUI application are welcome. If you have any suggestions or bug reports, please submit an issue on the GitHub repository. If you would like to contribute code, please submit a pull request.

Note: This is just a sample README file. You should modify it to fit your specific needs and changes.

---
### Commit History
* `v1.2.0`: Added three new parts to the application: Rename with Prefix, Add Suffix, and List Files
* `v1.1.0`: Fixed issue with buttons sometimes taking several clicks to work
* `v1.0.0`: Initial release of the File Renamer GUI application

### Known Issues
* None

### Future Development
* Add support for multiple file types
* Improve error handling for edge cases
* Add more features to the application

________________________________________________________________________________________________________________

##### Created by J Horsley III
[http://y2cl.net](y2cl.net)
