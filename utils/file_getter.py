import os
import time

from is_dir_complete import is_dir_complete
from is_file_complete import is_file_complete

def get_files():
    path = os.path.expanduser('~/Downloads')
    stack = []
    incomplete_files = []

    while True:
        dir_list = os.listdir(path)
        
        for file_name in dir_list:
            full_path = os.path.join(path, file_name)
            
            if os.path.isfile(full_path):
                if file_name not in incomplete_files and file_name not in [item[0] for item in stack]:
                    incomplete_files.append(file_name)
            elif os.path.isdir(full_path):
                if is_dir_complete(full_path):
                    if [file_name, "directory"] not in stack:
                        stack.append([file_name, "directory"])
                else:
                    if file_name not in incomplete_files:
                        incomplete_files.append(file_name)

        for file_name in incomplete_files.copy():
            full_path = os.path.join(path, file_name)
            if os.path.isfile(full_path):
                if is_file_complete(full_path) and not full_path.endswith('.crdownload') and not full_path.endswith('.part'):
                    stack.append([file_name, "file"])
                    incomplete_files.remove(file_name)
                else:
                    print(f"Still Completing {file_name}...")
            elif not os.path.exists(full_path):
                # If the file no longer exists, assume download was canceled
                print(f"File {file_name} no longer exists. Assuming download was canceled.")
                incomplete_files.remove(file_name)
            if os.path.isdir(full_path):
                if is_dir_complete(full_path):
                    stack.append([file_name, "directory"])
                    incomplete_files.remove(file_name)
                else:
                    print(f"Still Completing {file_name}...")
                    
        time.sleep(.3)  # Reasonable interval to avoid excessive CPU usage

        # Check if all files are either in the stack or being downloaded
        all_complete = all([file in [item[0] for item in stack] for file in dir_list])
        if not incomplete_files and all_complete:
            break  # Exit loop if all files are complete and stack is updated

    return stack