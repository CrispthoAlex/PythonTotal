from pathlib import Path, PureWindowsPath

folder_test = Path(
    'C:/Users/Holberton/CrispthoferRincon/udemy/PythonTotal/day_06/text_testing.txt'
)

print(folder_test.read_text())
"""
I'm first line
'Wow', I'm second line
Well done, I'm third line
"""
print(folder_test.name)  # text_testing.txt

print(folder_test.suffix)  # .txt

print(folder_test.stem)  # text_testing

print(folder_test.exists())  # True

print(folder_test.name)  # text_testing.txt

path_win = PureWindowsPath(folder_test)
print(path_win)
# C:\Users\Holberton\CrispthoferRincon\udemy\PythonTotal\day_06\text_testing.txt


