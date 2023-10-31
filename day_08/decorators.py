"""
Decorators
Functions to modify behavior from others functions

Example
def change_letters(action):

    def upper_text(text):
        print(text.upper())

    def lower_text(text):
        print(text.lower())

    "my_fn = upper_text
    my_fn("Python")"

    if action == "up":
        return upper_text
    elif action == 'low':
        return lower_text


operation = change_letters('up')
operation('words')


def a_function(function):
    return function


a_function(upper_text('Testing'))"""


def salute_decorator(function):

    def other_fn(word):
        print('Hello')
        function(word)
        print('Bye')

    return other_fn


# @salute_decorator
def upper_text(text):
    print(text.upper())


# @salute_decorator
def lower_text(text):
    print(text.lower())


upper_text('School')
lower_text('UNIVERSITY')
"""
Before decorator:
> SCHOOL
> university

After decorator:
Hello
SCHOOL
Bye
Hello
university
Bye
"""


mayusc_deco = salute_decorator(upper_text)
mayusc_deco('rice')
"""
Hello
RICE
Bye
"""
upper_text("rice")
# RICE
