import os
import time
from watchdog.observers import Observer


from scan_existing_files import scan_existing_files
from DownloadEventHandler import DownloadEventHandler

def monitor_downloads(path):
    # Scan existing files in the directory and initialize the file object
    files = scan_existing_files(path)
    
    # Print the initial state of the files
    print("Initial Files in Directory:")
    print(files)
    
    # Set up the event handler and observer
    event_handler = DownloadEventHandler(files)
    observer = Observer()
    
    # Schedule the observer to monitor the specified path
    observer.schedule(event_handler, path=path, recursive=False)
    
    # Start the observer to begin monitoring
    observer.start()
    
    try:
        # Keep the script running to monitor changes continuously
        while True:
            time.sleep(1)  # Sleep to reduce CPU usage while monitoring
    except KeyboardInterrupt:
        # Stop the observer if the user interrupts the program (Ctrl+C)
        observer.stop()
    
    # Ensure the observer thread is properly shut down
    observer.join()

# Main function to execute the monitoring
if __name__ == "__main__":
    # Get the path to the user's Downloads folder
    download_path = os.path.expanduser('~/Downloads')
    
    # Start monitoring the Downloads folder
    monitor_downloads(download_path)