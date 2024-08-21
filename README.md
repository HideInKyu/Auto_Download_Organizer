---

# Auto Download Organizer

Auto Download Organizer is a Python-based utility that automatically organizes your files from the `Downloads` folder into categorized subfolders based on their file types. It features duplicate file handling, dynamic folder creation, and a countdown timer that allows immediate access to downloaded files before organization.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation - Windows](#installation-windows)
4. [Installation - macOS](#installation-macos)
5. [Running the Script](#running-the-script)
6. [File Categories](#file-categories)
7. [Duplicate File Handling](#duplicate-file-handling)
8. [License](#license)

---

## Features

- **Automatic File Organization**: Moves downloaded files into categorized folders based on their file types (e.g., `Images`, `Videos`, `Documents`, `Audio`, etc.).
- **Wide File Type Support**: Handles common and specialized formats like `.jpg`, `.mp4`, `.pdf`, `.zip`, `.heic`, `.iso`, `.sql`, and more.
- **Duplicate File Handling**: Keeps the original file in the main folder and moves duplicates into a "Copy" folder, renaming them incrementally.
- **Countdown Timer**: Files remain in the `Downloads` folder for a specified amount of time after download, allowing immediate access before being moved.
- **Initial Folder Scan**: On first run, the script scans the `Downloads` folder and organizes all existing files.

---

## Requirements

- **Python 3.x**: Make sure Python is installed on your system.
- **Pip**: Python’s package manager.
- **`watchdog`**: A Python library used for monitoring file system events.

---

## Installation - Windows

### Step 1: Install Python

1. **Download Python**:
   - Go to the [Python website](https://www.python.org/downloads/) and click the yellow "Download Python 3.x.x" button.

2. **Run the Installer**:
   - During the installation, check the box that says **"Add Python to PATH"**, then click **Install Now**.

3. **Verify Python Installation**:
   - Open **Command Prompt** (search for "cmd" in the Start Menu) and type:
     ```bash
     py --version
     ```
   - You should see the Python version you installed (e.g., `Python 3.10.x`).

### Step 2: Install `pip` (If Not Installed)

1. **Check if `pip` is Installed**:
   - In the Command Prompt, type:
     ```bash
     py -m pip --version
     ```

2. **Install `pip` (If Not Installed)**:
   - Run the following command to install `pip`:
     ```bash
     py -m ensurepip --upgrade
     ```

### Step 3: Install Dependencies

1. **Install `watchdog`**:
   - In Command Prompt, run:
     ```bash
     py -m pip install watchdog
     ```

### Step 4: Set Up the Script to Run with a Custom Command

1. **Create a Batch File**:
   - Open **Notepad** and paste the following:
     ```batch
     @py C:\Users\YourUsername\Documents\File-Organization--main\utils\main.py %*
     ```
   - Replace `C:\Users\YourUsername\Documents\File-Organization--main` with the actual path to your script.
   - Save the file as `fileOrg.bat` in a folder like `C:\Users\YourUsername`.

2. **Add the Folder to PATH** (Optional):
   - Right-click on **This PC** and select **Properties** > **Advanced system settings** > **Environment Variables**.
   - Under **System Variables**, find **Path** and click **Edit**.
   - Click **New** and add the path where your `fileOrg.bat` is located.

3. **Run the Script**:
   - In Command Prompt, type:
     ```bash
     fileOrg
     ```

---

## Installation - macOS

### Step 1: Install Python

1. **Check if Python is Installed**:
   - Open **Terminal** (search for it in Spotlight) and type:
     ```bash
     python3 --version
     ```
   - If Python is not installed, install it via Homebrew:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     brew install python
     ```

### Step 2: Install `pip` (If Not Installed)

1. **Check if `pip` is Installed**:
   - Run:
     ```bash
     python3 -m pip --version
     ```

2. **Install `pip` (If Not Installed)**:
   - Run:
     ```bash
     python3 -m ensurepip --upgrade
     ```

### Step 3: Install Dependencies

1. **Install `watchdog`**:
   - Run:
     ```bash
     python3 -m pip install watchdog
     ```

### Step 4: Create an Alias for Easy Execution

1. **Open Terminal** and run:
   ```bash
   nano ~/.zshrc
   ```

2. **Add the Alias**:
   - Add the following line at the bottom of the file:
     ```bash
     alias fileOrg="python3 /path/to/File-Organization--main/utils/main.py"
     ```
   - Replace `/path/to/File-Organization--main` with the full path to your script.

3. **Save and Exit**:
   - Press `Ctrl + X`, then `Y`, and `Enter` to save the changes.

4. **Reload the Shell**:
   - Run:
     ```bash
     source ~/.zshrc
     ```

5. **Run the Script**:
   - Now, in the terminal, type:
     ```bash
     fileOrg
     ```

---

## Running the Script

### Windows

- If you've set up the batch file, simply run:
  ```bash
  fileOrg
  ```

- If you haven't created the batch file, navigate to the project folder and run:
  ```bash
  py utils/main.py
  ```

### macOS

- If you've set up the alias, simply run:
  ```bash
  fileOrg
  ```

- If you haven't set up the alias, navigate to the project folder and run:
  ```bash
  python3 utils/main.py
  ```

---

## File Categories

When the script runs, it automatically organizes files into the following categories:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.heic`, etc.
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, etc.
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xls`, `.ppt`, etc.
- **Audio**: `.mp3`, `.wav`, `.ogg`, etc.
- **Archives**: `.zip`, `.rar`, `.7z`, `.iso`, etc.
- **Executables**: `.exe`, `.msi`, `.bat`, `.sh`, etc.
- **Code/Script Files**: `.py`, `.js`, `.html`, etc.
- **Miscellaneous**: Any other unrecognized file types.

### Unrecognized File Types

Files that do not match any of the recognized categories will be moved to a `Misc` folder inside the `Organized` directory.

---

## Duplicate File Handling

- **Original File**: The first instance of a file remains in the main folder.
- **Duplicate Files**: If a file with the same name already exists, duplicates are placed in a folder named `<file name> Copy` and renamed as `file (1).ext`, `file (2).ext`, etc.

---

## License

This project is licensed under the MIT License.

---
