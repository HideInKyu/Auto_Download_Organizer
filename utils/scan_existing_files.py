import os

# Function to scan existing files and add them to the object
def scan_existing_files(path):
    files = {}
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        # Ignore hidden files
        if os.path.isfile(full_path) and not file_name.startswith('.'):
            # Get the file extension/type
            file_type = os.path.splitext(full_path)[1][1:]  # Extract file extension without the dot
            files[full_path] = file_type
    return files