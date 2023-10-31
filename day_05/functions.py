def myfirst_fn():
    """
    Print the text "My first function"
    :return:
    """
    print("My first function")


myfirst_fn()
# My first function


def hi_person(name):
    """
    Say hello to a person
    :param name: name of person
    :return:
    """
    print(f"Hi {name}")


hi_person("Mario")
hi_person("Louis")
"""
Hi Mario
Hi Louis
"""


def power_calc(number, exponential):
    """

    :param number: number to be powered
    :param exponential: Power to apply to the number
    :return: value of number to exponential
    """
    return number**exponential


print(power_calc(4, 20))
# 1099511627776


def multiply(num1, num2):
    """
    Multiply two numbers and return the result
    :param num1: number 1 to multiply
    :param num2: number 1 to multiply
    :return: result
    """
    return num1 * num2


print(multiply(45, 89))
# 4005
