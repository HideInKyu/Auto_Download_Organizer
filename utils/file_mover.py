import os
import shutil

# Function to create the "Organized" folder
def create_organized_folder():
    organized_dir = os.path.expanduser('~/Downloads/Organized')
    if not os.path.exists(organized_dir):
        os.makedirs(organized_dir)
    print("Organized folder created.")

# Function to handle duplicates by creating a "Copy" folder and moving the duplicate files there
def handle_file_duplicate(destination_folder, file_name):
    # Create a subfolder for the duplicates called "<file_name> Copy"
    base_name, extension = os.path.splitext(file_name)
    copy_folder_name = base_name + " Copy"
    copy_folder_path = os.path.join(destination_folder, copy_folder_name)
    
    # Ensure the copy folder exists
    if not os.path.exists(copy_folder_path):
        os.makedirs(copy_folder_path)
    
    return copy_folder_path

# Function to rename the duplicates inside the copy folder
def rename_file_in_copy_folder(copy_folder_path, file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1

    # Check for existing files and rename them incrementally inside the copy folder
    new_name = f"{base_name} ({counter}){extension}"
    while os.path.exists(os.path.join(copy_folder_path, new_name)):
        counter += 1
        new_name = f"{base_name} ({counter}){extension}"
    
    return new_name

# Function to move files based on type and handle duplicates
def move_files(files):
    organized_dir = os.path.expanduser('~/Downloads/Organized')
    files_folder = os.path.join(organized_dir, 'Files')

    # Ensure the "Files" folder exists for subfolders
    if not os.path.exists(files_folder):
        os.makedirs(files_folder)

    for full_path, file_type in files.items():
        # Skip any file or folder named "Organized"
        if 'Organized' in full_path:
            print(f"Skipping: {full_path} (belongs to 'Organized' folder)")
            continue

        file_name = os.path.basename(full_path)
        
        # Determine base category folder based on file type
        if file_type in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico', 'heic']:
            category_folder = 'Images'
        elif file_type in ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', 'vob', 'ogv', 'm4v', '3gp', '3g2', 'm2ts', 'mts', 'h264', 'rmvb', 'asf']:
            category_folder = 'Videos'
        elif file_type in ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma', 'aiff', 'mid', 'midi', 'oga', 'adpcm', 'm3u8']:
            category_folder = 'Audio'
        elif file_type in ['pdf', 'docx', 'doc', 'txt', 'rtf', 'odt', 'md', 'xls', 'xlsx', 'csv', 'ppt', 'pptx', 'ods', 'epub', 'mobi', 'azw', 'azw3', 'cbr']:
            category_folder = 'Documents'
        elif file_type in ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso', 'dmg', 'apk', 'appx', 'cab']:
            category_folder = 'Archives'
        elif file_type in ['exe', 'msi', 'bat', 'sh', 'app', 'deb', 'rpm', 'bin']:
            category_folder = 'Executables'
        elif file_type in ['ttf', 'otf', 'woff', 'woff2']:
            category_folder = 'Fonts'
        elif file_type in ['py', 'js', 'html', 'css', 'java', 'cpp', 'c', 'h', 'php', 'rb', 'pl', 'go', 'rs', 'ts', 'json', 'xml', 'yml']:
            category_folder = 'Code'
        elif file_type in ['dll', 'sys', 'inf', 'ini', 'log', 'cfg', 'plist', 'bak']:
            category_folder = 'System'
        elif file_type in ['epub', 'mobi', 'azw', 'azw3', 'pdf', 'fb2', 'lit', 'lrf']:
            category_folder = 'E-books'
        elif file_type in ['srt', 'ass', 'ssa']:
            category_folder = 'Subtitles'
        elif file_type in ['obj', 'fbx', 'stl', '3ds', 'blend']:
            category_folder = '3D Models'
        elif file_type in ['psd', 'ai', 'indd', 'fla', 'aep', 'prproj', 'veg']:
            category_folder = 'Projects'
        elif file_type in ['dwg', 'dxf', 'step', 'iges']:
            category_folder = 'CAD'
        elif file_type in ['sql', 'db', 'mdb', 'accdb']:
            category_folder = 'Databases'
        elif file_type in ['iso', 'img', 'vhd', 'vmdk']:
            category_folder = 'Disk Images'
        elif file_type in ['bak', 'bkp', 'backup']:
            category_folder = 'Backups'
        elif file_type in ['tmp', 'temp']:
            category_folder = 'Temp'
        elif file_type in ['shp', 'gdb', 'kml', 'geojson']:
            category_folder = 'GIS'
        elif file_type in ['sav', 'pak', 'dat', 'gcf', 'vpk']:
            category_folder = 'Games'
        elif file_type in ['mat', 'rdata', 'sas', 'sav']:
            category_folder = 'Scientific Data'
        else:
            category_folder = 'Misc'
        
        # Create the full path for the file type (e.g., /Documents/pdf)
        destination_folder = os.path.join(organized_dir, category_folder, file_type)
        
        # Ensure destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Check if the file already exists in the destination
        original_file_path = os.path.join(destination_folder, file_name)
        if os.path.exists(original_file_path):
            # Handle duplicate: Keep the original file in the parent folder and move the duplicates to the copy folder
            copy_folder_path = handle_file_duplicate(destination_folder, file_name)
            new_name = rename_file_in_copy_folder(copy_folder_path, file_name)
            # Move the duplicate file into the copy folder
            try:
                shutil.move(full_path, os.path.join(copy_folder_path, new_name))
                print(f"Moved duplicate: {full_path} to {os.path.join(copy_folder_path, new_name)}")
            except Exception as e:
                print(f"Error moving {full_path}: {e}")
        else:
            # Move the original file to the main destination folder
            try:
                shutil.move(full_path, original_file_path)
                print(f"Moved original file: {full_path} to {original_file_path}")
            except Exception as e:
                print(f"Error moving {full_path}: {e}")