import os
import shutil
import send2trash

print(os.getcwd())
"""
file_test = open('file_text_testing.txt', 'w')
file_test.write('texto de prueba')
file_test.close()
"""
print(os.listdir())
# ['collections_module.py', 'file_text_testing.txt', 'os_shutil_modules.py']

shutil.move('file_text_testing.txt', 'C:\\Users')
print(os.listdir())
# ['collections_module.py', 'os_shutil_modules.py']

"""
> remove files/folders
os.unlink()  # delete file from a path
os.rmdir()  # delete empty folder
shutil.rmtree()  # remove all from a path
"""

# send file removed to recycle folder
send2trash.send2trash('file_text_testing.txt')
print(os.listdir())
# ['collections_module.py', 'os_shutil_modules.py']

# Show all elements in a folder
print(os.walk('C:\\Users\\Home\\udemy\\PythonTotal'))
# <generator object _walk at 0x000001C0A5474EA0>

path_test = 'C:\\Users\\Home\\udemy\\PythonTotal'

for folder, sub_folder, file in os.walk(path_test):
    print(f'In folder: {folder}')
    print(f'The sub folders are:')
    for sub in sub_folder:
        if sub.startswith('day'):
            print(f'\t{sub}')
    print('The files are:')
    for fi in file:
        if fi.startswith('project'):
            print(f'\t{fi}')
    print()

