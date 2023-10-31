def devolver_distintos(*args):
    """
    Take up to 3 arguments of integer type,
    add (sum all) the arguments
    Ex:
        print(devolver_distintos(10, 2, 3))
        # 5.0
    :param args: arguments
    :return:
        - If sum total is greater than 15,
        return the max value
        - If sum total is less than 10,
        return min value
        - If sum total is between 10 y 15 (include),
        return mean value.
    """

    temp_args = list(args[:3])
    for n in temp_args:
        if not isinstance(n, int):
            print("All numbers will be integer")
            return
    sum_temp = sum(temp_args)
    if sum_temp in range(10, 16):
        temp_args.sort()
        return temp_args[1]
    elif sum_temp < 10:
        return min(temp_args)
    else:
        return max(temp_args)

