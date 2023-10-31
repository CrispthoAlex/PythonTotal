import os

"""
ruta = os.getcwd()
print(ruta)
// Current work directory
...\\udemy\\PythonTotal\\day_06
"""
"""
path_chdir = os.chdir('...udemy\\PythonTotal')
print(path_chdir)  # None
cur_path = os.getcwd()
print(f"This the current path {cur_path}")
file = open("text_edit_test.txt")
"""
"""
path_make = os.makedirs('C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_06\\makedir_test')
print(path_make)  # None"""

path_test = 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_06\\text_testing_2.txt'

element = os.path.basename(path_test)
print(element)  # text_testing_2.txt

element = os.path.dirname(path_test)
print(element)
# C:\Users\Holberton\CrispthoferRincon\udemy\PythonTotal\day_06

element = os.path.split(path_test)
print(element)
"""
(
    'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_06',
    'text_testing_2.txt'
)
"""

"""
path_remove = 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_06\\makedir_test'
os.rmdir(path_remove)"""

a_file = open('C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_06\\text_testing_1.txt')
print(a_file.read())

# Open file or folder with any OS
from pathlib_module import Path

folder_test = Path('C:/Users/Holberton/CrispthoferRincon/udemy/PythonTotal/day_06')
new_file = folder_test / 'text_testing.txt'

my_file = open(new_file)
print(my_file.read())
