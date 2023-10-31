def check_3_digits(num):
    return num in range(100, 1000)


number_check = 876
result = check_3_digits(number_check)
print(result)  # True


def check_3_digits_list(lis):
    for n in lis:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


num_list = [65, 97, 345, 988]
result_lis = check_3_digits_list(num_list)
print(result_lis)  # True


def check_3_digits_list1(lis):
    num_lis = []
    for n in lis:
        if n in range(100, 1000):
            num_lis.append(n)
        else:
            pass
    return num_list


num_list1 = [65, 97, 345, 988, 14, 765, 900, 23, 54, 100, 99, 345, 8765]
result_lis1 = check_3_digits_list1(num_list1)
print(result_lis1)
# [345, 988, 765, 900, 100, 345]

# showing tuples
coffe_price = [
    ('capuccino', 1.5),
    ('coffe frappe', 2.5),
    ('expresso', 1.2),
    ('mocha', 1.9)
]


def expensive_coffe(prices):
    price_expensive = 0
    coffe_name = ''
    for coffe, price in prices:
        if price > price_expensive:
            price_expensive = price
            coffe_name = coffe
        else:
            pass
    return coffe_name, price_expensive


print(expensive_coffe(coffe_price))
# ('coffe frappe', 2.5)

coffe, price = expensive_coffe(coffe_price)
print(f"Coffe more expensive is {coffe}, which value is USD{price}")
"""
Coffe more expensive is coffe frappe, which value is USD2.5
"""