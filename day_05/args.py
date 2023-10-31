def sum_nb(a, b):
    return a + b


print(sum_nb(5, 6))
# 11
"""
print(sum_nb(9, 6, 7))
          ^^^^^^^^^^^^^^^
TypeError: sum_nb() takes 2 positional arguments but 3 were given
"""


def sum_args(*args):
    total = 0
    for n in args:
        total += n
    return total


print(sum_args(9, 87, 6, 54, 5, 67))
# 228


def sum_args1(*args):
    return sum(args)


print(sum_args1(98, 76, 5, 45, 67, 8, 6, 4))
# 309


def num_person(*args):
    if isinstance(args[0], str):
        return f"{args[0]}, la suma de tus números es {sum(args[1:])}"
    else:
        return "Type first your name"


print(num_person("Laura", 87, 65, 67))

