tuple_test = (1, "A", "B", 3)
tuple_test2 = 1, 2, 3, 4, 5

print(type(tuple_test))  # <class 'tuple'>
print(type(tuple_test2))  # <class 'tuple'>

print(tuple_test[-2])  # B
print(tuple_test2[4])  # 5

# tuple_test[2] = 3
"""
tuple_test[2] = 3
TypeError: 'tuple' object does not support item assignment
"""
tuple_test3 = [0, 2, 4, 6, 8], "C", True
print(tuple_test3[0][4])  # 8

# casting
tuple_to_list = list(tuple_test)

print(tuple_to_list)  #  [1, 'A', 'B', 3]
print(type(tuple_to_list))  # <class 'list'>

# assigment tuple values to variables
var1, var2, var3 = tuple_test3
print(var1, var2, var3)
"""
[0, 2, 4, 6, 8]
C
True
"""
tuple_test.count()
