import os
from watchdog.events import FileSystemEventHandler

# Custom event handler to detect and track download statuses
class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self, files):
        self.files = files  # Initialize with existing files in the directory

    def on_created(self, event):
        # Only track files, not directories or hidden files (starting with '.')
        if not event.is_directory and not os.path.basename(event.src_path).startswith('.'):
            # If the file is a temporary download (e.g., .crdownload, .part)
            if event.src_path.endswith('.crdownload') or event.src_path.endswith('.part'):
                print(f"Download started: {event.src_path}")
            else:
                # When a file is created without those extensions, it's likely completed
                file_type = os.path.splitext(event.src_path)[1][1:]
                self.files[event.src_path] = file_type
                print(f"Download completed: {event.src_path}")
                print("Current Completed Files:", self.files)