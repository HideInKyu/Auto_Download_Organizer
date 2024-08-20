import os
import time

from file_getter import get_files

def download_check():
  zip = os.path.join(os.path.expanduser('~/Documents'), 'Compressed','Zip')


  filePath = {
    "zip" : zip,

  }
  files = get_files()

  print(files)

download_check()