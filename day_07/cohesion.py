"""
Weak cohesion
indicates that the relationship between the elements is low, and therefore they do not have a single functionality.
"""


def sum_weak():
    """
    This function ask  tho teh user for two numbers, then add them
    :return:
    """
    num1 = float(input("Choose a number"))
    num2 = float(input("Choose another number"))
    result = num1 + num2
    return result


"""
Strong cohesion
indicates that there is a high relationship between the existing elements within the module. This should be our goal
when designing programs.
"""


# example
def sum_strong(num1, num2):
    """
    This function just add number 1 and number 2
    :param num1: number 1
    :param num2: number 2
    :return:
    """
    result = num1 + num2
    return result


"""
The advantages of designing code with strong cohesion are:

Reduce the complexity  of the module, since it will have a smaller number of operations.
 Modules can be reused  more easily
The system will be easier  to maintain .
"""
