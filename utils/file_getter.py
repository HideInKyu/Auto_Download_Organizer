import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# CountdownTimer class definition
class CountdownTimer:
    def __init__(self, countdown_time, on_complete):
        self.countdown_time = countdown_time
        self.on_complete = on_complete
        self.timer_active = False
        self.last_time = None

    def start_timer(self):
        self.timer_active = True
        self.last_time = time.time()

    def reset_timer(self):
        print("Resetting timer.")
        self.start_timer()

    def check_timer(self):
        if self.timer_active and (time.time() - self.last_time) >= self.countdown_time:
            print("Timer completed. Executing on_complete function.")
            self.timer_active = False
            self.on_complete()

# Event handler to track new files being created
class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self, files, countdown_timer):
        self.files = files
        self.countdown_timer = countdown_timer
        self.incomplete_files = []

    def on_created(self, event):
        if not event.is_directory and not os.path.basename(event.src_path).startswith('.'):
            if event.src_path.endswith('.crdownload') or event.src_path.endswith('.part'):
                self.incomplete_files.append(event.src_path)
                print(f"Download started: {event.src_path}")
            else:
                file_type = os.path.splitext(event.src_path)[1][1:]
                self.files[event.src_path] = file_type
                print(f"File detected: {event.src_path} ({file_type})")
                self.countdown_timer.reset_timer()

    def on_modified(self, event):
        if not event.is_directory and event.src_path in self.incomplete_files:
            if not event.src_path.endswith('.crdownload') and not event.src_path.endswith('.part'):
                self.incomplete_files.remove(event.src_path)
                file_type = os.path.splitext(event.src_path)[1][1:]
                self.files[event.src_path] = file_type
                print(f"Download completed: {event.src_path} ({file_type})")
                self.countdown_timer.reset_timer()

# Function to monitor downloads and trigger the countdown timer
def monitor_downloads(download_path, files, countdown_timer):
    event_handler = DownloadEventHandler(files, countdown_timer)
    observer = Observer()

    observer.schedule(event_handler, path=download_path, recursive=False)
    observer.start()

    try:
        while True:
            countdown_timer.check_timer()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Function to scan for existing files in the Downloads folder
def scan_existing_files(download_path):
    files = {}
    existing_items = os.listdir(download_path)

    for item in existing_items:
        full_path = os.path.join(download_path, item)
        if os.path.isfile(full_path) and not item.startswith('.'):
            file_type = os.path.splitext(full_path)[1][1:]  # Get file extension without dot
            files[full_path] = file_type
        elif os.path.isdir(full_path) and not item.startswith('.'):
            # Detect directories that may need to be moved to "Files"
            files[full_path] = 'directory'
    
    return files