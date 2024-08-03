import os

path = os.path.expanduser('~/Downloads')
dir_list = os.listdir(path)


# Shows all contents of download file and shows if its a file or a directory
for file_name in dir_list:
    full_path = os.path.join(path, file_name)  # Join the directory path with the file name so that isfile and isdir works properly
    if os.path.isfile(full_path):
        # splits up the file name to name and extension
        split_tup = os.path.splitext(file_name)
        file_name = split_tup[0]
        file_ext = (split_tup[1]).lower()
        print("File Name: ", file_name)
        print("File Extension: ", file_ext)
    elif os.path.isdir(full_path):
        print("Dir Name: ", file_name)
