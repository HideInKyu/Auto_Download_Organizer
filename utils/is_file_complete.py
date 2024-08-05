import os
import time

def is_file_complete(file_path):
    try:
        initial_size = os.path.getsize(file_path)
        time.sleep(.3)
        new_size = os.path.getsize(file_path)
        return initial_size == new_size
    except FileNotFoundError:
        # File not found, possibly still downloading
        return False