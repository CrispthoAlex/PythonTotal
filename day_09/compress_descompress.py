import zipfile
import os
import shutil


my_zip = zipfile.ZipFile('compressed_file.zip', 'w')

my_zip.write('mi_texto_A.txt')
my_zip.write('mi_texto_B.txt')

my_zip.close()

print(os.listdir(os.getcwd()))
# [                          ~~~~~~~~~~~~~~~~~~~~
#   'collections_module.py', 'compressed_file.zip', 'compress_descompress.py',
#   'datetime_module.py', 'file_text_testing.txt', 'math_module.py', 'mi_texto_A.txt',
#   'mi_texto_B.txt', 'os_shutil_modules.py', 'regexp_module.py', 'time_metrics.py', '__pycache__'
# ]

zip_open = zipfile.ZipFile('compressed_file.zip', 'r')
zip_open.extractall()
zip_open.extract()

folder_origin = 'C:\\Users\\Home\\PythonTotal\\day_09\\text_files'
file_destiny = 'text_folder_compressed'

# compress
shutil.make_archive(file_destiny, 'zip', folder_origin)
# decompress
shutil.unpack_archive('text_folder_compressed.zip', 'Extract_done', 'zip')


