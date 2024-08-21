import os
import time
from file_mover import create_organized_folder, move_files
from file_getter import monitor_downloads, CountdownTimer, scan_existing_files

def on_timer_complete():
    global files
    print("Timer completed. Moving files...")
    if files:  # Check if there are files to move
        move_files(files)
        files.clear()
    else:
        print("No files to move.")

def initial_scan_and_process(download_path):
    global files

    # Scan the directory for any existing files or folders
    files = scan_existing_files(download_path)
    
    if files:
        print(f"Initial files and folders detected: {files}")
        print("Starting countdown for initial file processing...")

        # Countdown before moving initial files and folders
        for i in range(10, 0, -1):
            print(f"{i} seconds remaining before organizing initial files...")
            time.sleep(1)
        
        # Move the initial files after countdown
        on_timer_complete()
    else:
        print("No initial files or folders detected.")

def main():
    global files
    files = {}

    create_organized_folder()
    download_path = os.path.expanduser('~/Downloads')

    # Scan for initial files and organize them after countdown
    initial_scan_and_process(download_path)

    # Initialize the countdown timer for future downloads
    countdown_timer = CountdownTimer(countdown_time=600, on_complete=on_timer_complete)

    # Monitor new downloads and handle them with the countdown timer
    monitor_downloads(download_path, files, countdown_timer)

if __name__ == "__main__":
    main()