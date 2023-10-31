"""
Only read the file
file_test = open("text_testing.txt", 'r')

If exist file, write the file (replace lines) else create a new file
file_test = open("text_testing_1.txt", 'w')

# Add a new text line at the end of file
file_test = open("text_testing_1.txt", 'a')

file_test.writelines('''Hello
world
I'm
a new
line
''')
"""

file_test = open("text_testing_2.txt", 'a')

line_list = ["\nHello", "there,", "We're", "others new", "lines"]
for li in line_list:
    print(f"'{li}' will be write in file_test")
    file_test.writelines(li + ' ')

file_test.close()


