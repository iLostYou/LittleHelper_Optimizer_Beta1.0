import time

print("                                                            ")
print("     __    _ __  __  __        __  __     __                ")
print("    / /   (_) /_/ /_/ /__     / / / /__  / /___  ___  _____ ")
print("   / /   / / __/ __/ / _ \   / /_/ / _ \/ / __ \/ _ \/ ___/ ")
print("  / /___/ / /_/ /_/ /  __/  / __  /  __/ / /_/ /  __/ /     ")
print(" /_____/_/\__/\__/_/\___/  /_/ /_/\___/_/ .___/\___/_/      ")
print("                                       /_/                  ")
print("                                                            ")                                                        
                                                              

import os
import shutil
import tempfile
import errno

def clean_temporary_files():
    temp_folders = [
        tempfile.gettempdir(),                            # User temporary folder
        os.path.join(os.environ.get("SystemRoot"), "Temp") # System temporary folder
    ]

    deleted_files = 0
    deleted_folders = 0

    for temp_folder in temp_folders:
        for root, dirs, files in os.walk(temp_folder, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    deleted_files += 1
                except OSError as e:
                    if e.errno == errno.EACCES:  # File in use, skip deletion
                        print(f"Skipped file (in use): {file_path}")
                    else:
                        print(f"Failed to delete file: {file_path} ({e})")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted folder: {dir_path}")
                    deleted_folders += 1
                except OSError as e:
                    print(f"Failed to delete folder: {dir_path} ({e})")

    print(f"Total files deleted: {deleted_files}")
    print(f"Total folders deleted: {deleted_folders}")

# Rest of the code...

# Clean temporary files
clean_temporary_files()

