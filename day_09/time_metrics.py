import time
import timeit


def for_test(num):
    list_a = []
    for nb in range(1, num + 1):
        list_a.append(nb)
    return list_a


def while_test(num):
    list_a = []
    counter = 1
    while counter <= num:
        list_a.append(counter)
        counter += 1
    return list_a


# time execution for loop
start = time.time()
print(for_test(1500))
end = time.time()
print(end - start)

# time execution while loop
start = time.time()
print(while_test(1500))
end = time.time()
print(end - start)


declaration = """
for_test(1500)
"""

def_setup = """
def for_test(num):
    list_a = []
    for nb in range(1, num + 1):
        list_a.append(nb)
    return list_a
"""

time_for = timeit.timeit(declaration, def_setup, number=100000)
print(f'Time for execution\n{time_for}')
"""
Time for execution
9.758797800000139
"""

declaration2 = """
while_test(1500)
"""

def_setup2 = """
def while_test(num):
    list_a = []
    counter = 1
    while counter <= num:
        list_a.append(counter)
        counter += 1
    return list_a
"""

time_while = timeit.timeit(declaration2, def_setup2, number=100000)
print(f'Time while execution\n{time_while}')
"""
Time while execution
13.793840700000146
"""


