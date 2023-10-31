import os
from pathlib import Path
import re
import datetime
import time
import math


""" 
Searching series number
Create a searching series number. ¿What is that? It's a program that search series number achieve a 
format, inside a folder tree.

# Flow
    # Iterating inside folders

    # Open text file and read lines
        # search in text line the series pattern
        # [N] + [three chars] + [-] + [five numbers]
        # Example: Nryu-12365
    # Return list of files with pattern OK


# Print the result table:

----------------------------------------------------
Search date: [today]

FILE		NRO. SERIES
-------		----------
text_1.txt	Nter-15496
text_25.txt	Ngba-85235

Numbers found: 2
Lapsed search: 1 seconds
----------------------------------------------------
"""

start = time.time()
# Iterating inside folders
PATH_FOLDER = Path(os.getcwd(), 'PD_09_instructions\\Mi_Gran_Directorio')
TODAY = datetime.date.today().strftime('%d/%m/%Y')
PATTERN = r'N\w{3}-\d{5}'


def check_text_file(path_file, list_files, file):
    """
    Append the file to the list_files if pattern in the line exist
    :param path_file: path to check if file exist
    :param list_files: list to be filled with file and series number tuple
    :param file: name file to append to the list_files
    """
    read_file = open(path_file, 'r')
    # Check pattern
    check = re.search(PATTERN, read_file.readline())
    if check is not None:
        list_files.append((file, check.group()))
    read_file.close()


def iterate_inside_folders(path_folder) -> list:
    """
    Iterate in the folders, sub folders and files
    :param path_folder: main path where the files will be listed
    :return: A list with the files with pattern checked true
    """
    files_found = []
    for folder, sub_folder, file in os.walk(path_folder):
        # Iterate files
        for idx, fi in enumerate(file):
            path_file = Path(folder, fi)
            # fill the list of files with series number
            check_text_file(path_file, files_found, fi)
    return files_found


def string_series_found(series: list) -> str:
    """
     Create a string with the files and series number found
    :param series: list of file with a series number in
    """
    list_to_print = ''
    for idx, txt in enumerate(series):
        list_to_print += f'\t{idx + 1}\t{txt[0]}\t{txt[1]}\n'
    return list_to_print


def show_result():

    result: list = iterate_inside_folders(PATH_FOLDER)
    end = time.time()
    # Print result table:
    print(f"""
    ----------------------------------------------------
    Search date: {TODAY}
    
    #    FILE		    NRO. SERIES
    --- --------------  ----------
{string_series_found(result)}
    Numbers found: {len(result)}
    Lapsed search: {math.ceil(end-start)} seconds
    ----------------------------------------------------
    """)


show_result()

