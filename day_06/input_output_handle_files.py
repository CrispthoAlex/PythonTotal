file_test = open('text_testing.txt')

# print(file_test.read())


"""line = file_test.readline()
print(line)
line = file_test.readline()
print(line.rstrip())
line = file_test.readline()
print(line)"""

"""for li in file_test:
    print(f"Loop line {li}")
    print(f"Upper line {li.upper()}")"""

lines = file_test.readlines()
# lines.pop()
print(lines)

file_test.close()
