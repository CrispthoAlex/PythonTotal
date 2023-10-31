def zero_count(*args):
    """
    Receive an indefinite number of arguments
    Ex:
        print(zero_count(87, 67, 5, 67, 0, 98, 6, 7, 0))
        # False
    :param args: numbers
    :return:
        - Return true if zero (0) number is consecutive
    """
    for n in args:
        if (n == 0 and
                args[args.index(n) + 1] == 0):
            return True
    return False
