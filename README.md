# Auto Download Organizer

Auto Download Organizer is a Python utility that automatically categorizes and organizes files from your `Downloads` folder into appropriate sub-folders based on their file types. It features duplicate file handling, dynamic folder creation, and a countdown timer to allow immediate access to downloaded files before organization.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Categories](#file-categories)
6. [Duplicate File Handling](#duplicate-file-handling)
7. [Customization](#customization)
8. [License](#license)

## Features

- **Automatic File Organization**: Moves downloaded files into categorized sub-folders based on their file types (e.g., `Images`, `Videos`, `Documents`, `Audio`, etc.).
- **Dynamic Folder Creation**: Automatically creates new folders when a new file type is detected.
- **Wide Range of Supported File Types**: Handles popular and specialized file formats such as `.jpg`, `.mp4`, `.pdf`, `.zip`, `.heic`, `.iso`, `.sql`, `.obj`, and more.
- **Duplicate File Handling**: Keeps the original file in the main folder and moves duplicates into a `Copy` folder, renaming them incrementally (e.g., `file (1).pdf`, `file (2).pdf`).
- **Countdown Timer**: Files stay in the `Downloads` folder for a specified time after download to allow immediate access. The timer resets if a new download is detected during the countdown.
- **Initial Scan**: When the script is first run, it scans the `Downloads` folder and organizes all existing files.
- **Shell Integration**: The script can be executed using the custom command `fileOrg` in your terminal.

## Requirements

- Python 3.x
- Python Libraries:
  - `watchdog`
  - `shutil`
  
To install the necessary dependencies, run the following:

```bash
pip install watchdog
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/auto-download-organizer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd auto-download-organizer
   ```

3. **Set up an alias for easy execution**:
   Add the following alias to your shell configuration file (`.zshrc` or `.bashrc`):
   ```bash
   alias fileOrg='/usr/local/bin/python3 /path-to-your-project-directory/utils/main.py'
   ```
   Replace `/path-to-your-project-directory/` with the actual path to the project.

4. **Reload your shell configuration**:
   ```bash
   source ~/.zshrc  # For zsh users
   source ~/.bashrc  # For bash users
   ```

5. **Make the script executable** (optional):
   If you prefer to run the script directly as an executable, follow these steps:
   ```bash
   chmod +x /path-to-your-project-directory/utils/main.py
   sudo mv /path-to-your-project-directory/utils/main.py /usr/local/bin/fileOrg
   ```

## Usage

To start the Auto Download Organizer, simply run:

```bash
fileOrg
```

The script will begin monitoring your `Downloads` folder, organizing files based on their types, and handling duplicates accordingly.

### Custom Commands

- **Start Organization**: 
  ```bash
  fileOrg
  ```
  This command starts the organization process, scanning and moving files from the `Downloads` folder.

## File Categories

The script organizes files into the following categories:

- **Images**: `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`, `.heic`, etc.
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m2ts`, etc.
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`, `.wma`, etc.
- **Documents**: `.pdf`, `.docx`, `.doc`, `.txt`, `.rtf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.epub`, `.mobi`, etc.
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.iso`, `.dmg`, etc.
- **Executables**: `.exe`, `.bat`, `.sh`, `.app`, `.msi`, etc.
- **Fonts**: `.ttf`, `.otf`, `.woff`, `.woff2`
- **Code/Script**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, etc.
- **System Files**: `.dll`, `.sys`, `.log`, `.inf`, `.cfg`
- **Other Categories**: 3D Models, GIS files, CAD files, Databases, Disk Images, and more.

### Unrecognized File Types

If the script encounters an unrecognized file type, it will be moved to the `Misc` folder.

## Duplicate File Handling

- **Original File**: The first instance of a file remains in the appropriate category folder.
- **Duplicate Files**: If a file with the same name already exists, duplicates are moved to a folder named after the original file with "Copy" appended (e.g., `100MB Copy`), and renamed incrementally (e.g., `100MB (1).bin`, `100MB (2).bin`).

## Customization

### Countdown Timer

By default, the script waits for 10 seconds before moving downloaded files. You can customize this value by modifying the `CountdownTimer` class in the `file_getter.py` script.

### File Categories

The current file categories and supported file types are defined in the `move_files` function in `file_mover.py`. You can add or modify these categories based on your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
