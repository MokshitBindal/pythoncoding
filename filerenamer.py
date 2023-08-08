import os
import re


def rename_files(directory, pattern, replacement=''):
    for filename in os.listdir(directory):
        if re.search(pattern, filename):
            new_filename = re.sub(pattern, replacement, filename)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)


if __name__ == "__main__":
    # Set the directory where your files are located
    directory = 'C:\\Users\\moksh\\Downloads'

    # Define the regular expression pattern for the part of the filename you want to remove
    pattern_to_remove = r'[FreeCourseSite.com] Udemy - '

    # Optionally, you can set the replacement string, leave it empty to just remove the matched part
    replacement_string = ''

    # Call the function to rename the files
    rename_files(directory, pattern_to_remove, replacement_string)
