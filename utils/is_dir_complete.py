import os
import time

def is_dir_complete(dir_path):
    initial_files = set(os.listdir(dir_path))
    time.sleep(.3) 
    new_files = set(os.listdir(dir_path))
    return initial_files == new_files