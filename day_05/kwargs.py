def sum_nb(**kwargs):
    print(type(kwargs))

sum_nb(x=3, y=9, z=9)
# <class 'dict'>


def sum_nb1(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        total += value
    return total

print(sum_nb1(x=35, y=8, z=19))
"""
x = 35
y = 8
z = 19
62
"""

# powerfull fn
def sum_powerful(num1, num2, *args, **kwargs):
    print(f"first value is {num1}")
    print(f"second value is {num2}")
    for arg in args:
        print(f"arg[{args.index(arg)}] = {arg}")

    for key, value in kwargs.items():
        print(f"{key} = {value}")


sum_powerful(19, 23,
             9, 87, 456, 4, 56, 87, "test1", "test2",
             x="one", y="two", z="three"
             )
"""
first value is 19
second value is 23
arg[0] = 9
arg[1] = 87
arg[2] = 456
arg[3] = 4
arg[4] = 56
arg[1] = 87
arg[6] = test1
arg[7] = test2
x = one
y = two
z = three
"""

test_args = [19, 7, 56, 40, 6, 7]
test_kwargs = {
    "x": "nine",
    "y": "eleven",
    "z": "twenty"
}

sum_powerful(55, 6, *test_args, **test_kwargs)
"""
first value is 55
second value is 6
arg[0] = 19
arg[1] = 7
arg[2] = 56
arg[3] = 40
arg[4] = 6
arg[1] = 7
x = nine
y = eleven
z = twenty
"""
