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
import subprocess
import tempfile

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
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    deleted_files += 1
                except Exception as e:
                    print(f"Failed to delete file: {file_path} ({e})")

            for dir in dirs:
                try:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path)
                    print(f"Deleted folder: {dir_path}")
                    deleted_folders += 1
                except Exception as e:
                    print(f"Failed to delete folder: {dir_path} ({e})")

    print(f"Total files deleted: {deleted_files}")
    print(f"Total folders deleted: {deleted_folders}")

def optimize_startup_programs():
    # Implement your logic to optimize startup programs here
    print("Optimizing startup programs...")

def tweak_system_settings():
    # Example: Change the power plan to 'High Performance'
    try:
        subprocess.run(['powercfg', '-setactive', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'])
        print("Changed power plan to 'High Performance'.")
    except Exception as e:
        print(f"Failed to tweak system settings: {e}")

def display_menu():
    print("Windows Optimizer Menu:")
    print("1. Clean Temporary Files")
    print("2. Optimize Startup Programs")
    print("3. Tweak System Settings")
    print("4. Exit")
    print("5. Discord")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        clean_temporary_files()
    elif choice == "2":
        optimize_startup_programs()
    elif choice == "3":
        tweak_system_settings()
    elif choice == "4":
        print("Exiting...")
        break
    elif choice == "5":
        print("discord.gg/YhH9GyZdmk.")
    else:
        print("Invalid choice. Please try again.")
