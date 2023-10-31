lista_1 = ["a", "b", "c", "d", "e", "f"]
idx = 0
for item in lista_1:
    print(idx, item)
    idx += 1
"""
0 a
1 b
2 c
3 d
4 e
5 f
"""

for tup in enumerate(lista_1):
    # item as a tuple
    print(tup)
"""
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
(5, 'f')
"""

for idx, item in enumerate(lista_1):
    print(idx, item)
"""
0 a
1 b
2 c
3 d
4 e
5 f
"""

tuple_list = list(enumerate(range(0, 50, 3)))
print(tuple_list)
"""
[
    (0, 0), (1, 3), (2, 6), (3, 9), (4, 12), (5, 15),
    (6, 18), (7, 21), (8, 24), (9, 27), (10, 30), (11, 33),
    (12, 36), (13, 39), (14, 42), (15, 45), (16, 48)
]
"""
