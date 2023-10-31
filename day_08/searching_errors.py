"""
This a module to show searching errors in python
pip install pylint
_______________________________________________

|> pylint searching_errors.py -r y

first review
************* Module searching_errors
searching_errors.py:12:0: C0305: Trailing newlines (trailing-newlines)
searching_errors.py:9:0: C0103: Constant name "number1" doesn't conform t
o UPPER_CASE naming style (invalid-name)
searching_errors.py:10:6: E0602: Undefined variable 'Number1' (undefined-
variable)
....

-----------------------------------
Your code has been rated at 0.00/10

##########################################
second review

************* Module searching_errors
searching_errors.py:27:0: C0116: Missing function or method docstring (missing-function-docstrin
g)
....

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 0.00/10, +7.50)

###########################################################
third review

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.50/10, +2.50)

"""

# first code evaluated
# number1 = 600
# print(Number1)


def a_function():
    """
    This function just print a number
    :return: None
    """
    number1 = 1000
    print(number1)


a_function()
