def return_four():
    return 4


def generator1():
    yield 4


print(return_four())
print(generator1())
"""
4
<generator object my_generator at 0x0000026299928880>
"""

gen = generator1()

print(next(gen))
# 4
"""
> print(next(gen))
Traceback (most recent call last):
  File 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_08\\generators.py', line 19, in <module>
    print(next(gen))
          ^^^^^^^^^
StopIteration
"""
# ================================================================


def return_list10():
    list10 = [x * 10 for x in range(1, 5)]
    return list10


def generator2():
    for x in range(1, 5):
        yield x * 10


gen_2 = generator2()

print(return_list10())
# [10, 20, 30, 40]
print(next(gen_2))
# 10
print(next(gen_2))
# 20
print(next(gen_2))
# 30
print(next(gen_2))
# 40
"""
> print(next(gen_2))
Traceback (most recent call last):
  File 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_08\\generators.py', line 53, in <module>
    print(next(gen_2))
          ^^^^^^^^^^^
StopIteration
"""

# ================================================================


def generator3():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


gen_3 = generator3()

print(next(gen_3))
print(next(gen_3))
print('Testing more code')
print(next(gen_3))
"""
1
2
Testing more code
3
"""


# =============================================================================
# PRACTICE

def generator1():
    x = 0
    while True:
        x += 1
        yield x


gen_4 = generator1()


def generator2():
    x = 1
    while True:
        yield x * 7
        x += 1


gen_5 = generator2()


def generator_life():
    life = 4

    while life > 0:
        life -= 1
        if life == 3:
            yield "3 lives left"
        elif life == 2:
            yield "2 lives left"
        elif life == 1:
            yield "1 life left"
    yield "Game Over"


lost_life = generator_life()



