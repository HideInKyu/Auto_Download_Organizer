import os

path = os.path.expanduser('~/Downloads')
dir_list = os.listdir(path)

for file_name in dir_list:
    print(file_name)