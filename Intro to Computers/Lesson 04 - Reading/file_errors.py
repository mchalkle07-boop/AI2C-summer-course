# Exercise 10: FileNotFoundError - Missing Files
# Goal: Handle file-related errors properly.

# Create file_errors.py:

import os

# Combined file list to process sequentially
files_to_read = ["nonexistent_file.txt", "data/info.txt"]

for filename in files_to_read:
    print(f"\n--- Attempting to read: {filename} ---")
    try:
        # attempt file opening without pre-checking
        with open(filename, "r") as file:
            content = file.read()
            print("Content successfully read:")
            print(content)
            
    except FileNotFoundError:
        # Handles both missing files and missing parent directories
        print(f"Error: The system cannot find the path or file: '{filename}'")
        print(f"Current working directory: {os.getcwd()}")
        
    except Exception as e:
        # Catch-all for other unexpected issues (e.g., permission errors)
        print(f"An unexpected error occurred: {e}")
