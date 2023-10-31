test_set = set({1, 2, 2, 3, 4, 5, 6, 7, 8, 8})
test_set2 = {"a", "b", "c", "d", "e", "f"}
# test_set3 = {True, "A", 10, [9, 8, 7]}
"""
test_set3 = {True, "A", 10, [9, 8 , 7]}
TypeError: unhashable type: 'list'
"""

# test_set4 = {{"A": 1, "B": 2}, True, 4}
"""
test_set4 = {{"A": 1, "B": 2}, True, 4}
TypeError: unhashable type: 'dict'
"""

print(test_set, type(test_set))
# {1, 2, 3, 4, 5, 6, 7, 8}
# <class 'set'>

print(test_set2, type(test_set2))
# {'b', 'f', 'c', 'a', 'd', 'e'}
# <class 'set'>

# print(test_set2[0])
"""
print(test_set2[0])
TypeError: 'set' object is not subscriptable
"""

test_set5 = {"a", "b", "c", (1, 2, 3, 4, 5), "b", "c"}
print(test_set5, type(test_set5))
# {'c', 'a', (1, 2, 3, 4, 5), 'b'}
# <class 'set'>

print(len(test_set))  # 8
print("a" in test_set5)  # True

test_set6 = test_set.union(test_set2)
print(test_set6)
# {1, 2, 3, 4, 5, 6, 7, 8, 'c', 'a', 'b', 'd', 'e', 'f'}

test_set6.add((True, False))
print(test_set6)
# {'f', 1, 2, 3, 4, 5, 6, 7, 8, 'e', 'd', 'a', (True, False), 'b', 'c'}

test_set6.remove((True, False))
print(test_set6)
# {1, 2, 3, 4, 5, 6, 7, 8, 'b', 'd', 'f', 'e', 'a', 'c'}

test_set6.discard("f")
print(test_set6)
# {1, 2, 3, 4, 5, 6, 7, 8, 'd', 'b', 'a', 'e', 'c'}

test_set6.pop()
print(test_set6)
# {2, 3, 4, 5, 6, 7, 8, 'a', 'e', 'b', 'd', 'c'}

test_set6.clear()
print(test_set6)
# set()


