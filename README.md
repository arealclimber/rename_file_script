# File Renaming and Moving Tool

This is a simple Python script for batch renaming files and moving them from one folder to another.

## Features

- Read files from a specified source folder
- Exclude specific files (e.g., .DS_Store)
- Sort files by name
- Rename files to a specified format (e.g., report_thumbnail_1.png)
- Copy renamed files to a destination folder
- Preserve original file extensions

## Folder Structure

```
rename_file_script
├─ 📁input
├─ 📁output
├─ 📄README.md
└─ 📄main.py
```

## Usage

1. Ensure you have Python 3.x installed.
2. Download the `rename_file_script` folder.
3. Create a folder named `input` and place your files in it.
4. Run the script:

   ```
   cd rename_file_script
   python3 main.py
   ```

5. When prompted, enter the desired prefix for the renamed files (or press Enter to use the default "report_thumbnail").

## Notes

- The script will automatically create the destination folder if it doesn't exist.
- If files with the same names already exist in the destination folder, they will be overwritten.
- The script will skip .DS_Store files.
- The script uses relative paths for input and output folders. Make sure you have "input" and "output" folders in the same directory as the script.

## Optional Feature

The script includes a commented-out `rename_files` function that can rename files directly in a specified folder without copying them to a new folder. If you need this functionality, uncomment the relevant code and modify as needed.

## Contributing

Suggestions and improvements are welcome! Feel free to submit pull requests or open issues.
