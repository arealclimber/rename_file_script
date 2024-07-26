import os
import shutil

# Fixed input and output folders
def rename_and_move_files(source_folder, destination_folder, prefix):
    # Ensure the source folder path exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist")
        return

    # Ensure the destination folder exists, create if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder '{destination_folder}'")

    # Define files to exclude
    excluded_files = ['.DS_Store']

    # Get all files from the source folder, excluding specified files
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f not in excluded_files]

    # Sort file names
    files.sort()

    # Rename files and move to destination folder
    for index, file in enumerate(files, start=1):
        old_path = os.path.join(source_folder, file)
        new_name = f"{prefix}_{index}{os.path.splitext(file)[1]}"
        new_path = os.path.join(destination_folder, new_name)

        try:
            shutil.copy2(old_path, new_path)
            print(f"Copied and renamed '{file}' to '{new_name}'")
        except Exception as e:
            print(f"Error processing '{file}': {str(e)}")

# Set source and destination folder paths as relative paths
source_folder = "input"
destination_folder = "output"

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Convert relative paths to absolute paths
source_folder = os.path.join(current_dir, source_folder)
destination_folder = os.path.join(current_dir, destination_folder)

# Get prefix from user input
prefix = input("Enter file name prefix (default is 'report_thumbnail'): ") or "report_thumbnail"

rename_and_move_files(source_folder, destination_folder, prefix)