from collections import Counter, defaultdict, namedtuple, deque

#################################################################################
#                             Counter module                                    #
#################################################################################
numbers = [1,1,1,1,2,2,2,4,4,4,4,5,5,5,5,9,9,9,9,0,0,0,0,3,3,3,3]
print(Counter(numbers))
# Counter({
#   1: 4, 4: 4, 5: 4, 9: 4, 0: 4, 3: 4, 2: 3
# })

text = 'To the bread bread and to the wine wine'
print(Counter(text))
# Counter({
#   ' ': 8, 'e': 6, 't': 3, 'a': 3, 'd': 3, 'n': 3, 'o': 2, 'h': 2,
#   'b': 2, 'r': 2, ',': 2, 'w': 2, 'i': 2, 'T': 1
# })

print(Counter(text.lower().split()))
# Counter({'to': 2, 'the': 2, 'bread': 2, 'wine': 2, 'and': 1})

series = Counter([5,5,5,5,5,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,9,9,9])
print(series.most_common())
# [(5, 8), (7, 5), (6, 4), (8, 3), (9, 3)]
print(series.most_common(1))
# [(5, 8)]
print(series.most_common(2))
# [(5, 8), (7, 5)]
print(series.most_common(4))
# [(5, 8), (7, 5), (6, 4), (8, 3)]

# casting the series
print(list(series))
# [5, 6, 7, 8, 9]
print(series.values())
# dict_values([8, 4, 5, 3, 3])
print(series.subtract([1,2,3,4]))
# None
print(series)
# Counter({
#   5: 8, 7: 5, 6: 4, 8: 3, 9: 3, 1: -1, 2: -1, 3: -1, 4: -1
# })
ele = series.elements()
print(ele)
# <itertools.chain object at 0x0000016E7757BD30>
print(series.copy())
# Counter({
#   5: 8, 7: 5, 6: 4, 8: 3, 9: 3, 1: -1, 2: -1, 3: -1, 4: -1
# })
print(series.items())
# dict_items([
#   (5, 8), (6, 4), (7, 5), (8, 3), (9, 3), (1, -1),
#   (2, -1), (3, -1), (4, -1)
# ])
print(series.clear())
# None
print(series)
# Counter()
series.items()

#################################################################################
#                               defaultdict                                     #
#################################################################################

test_dict = {'A': 1, 'B': 2, 'C': 3}
"""
> print(test_dict['D'])

Traceback (most recent call last):
  File 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_09\\collections_module.py', line 67, in <module>
    print(test_dict['D'])
          ~~~~~~~~~^^^^^
KeyError: 'D'
"""
dict_2 = defaultdict(lambda: 'empty key')
print(dict_2)
# defaultdict(<function <lambda> at 0x0000020A96CA04A0>, {})
dict_2['E'] = 5
dict_2['F'] = 6
print(dict_2['G'])
# empty key
print(dict_2)
# defaultdict(
#   <function <lambda> at 0x0000028E3C1504A0>,
#   {'E': 5, 'F': 6, 'G': 'empty key'}
# )
print(defaultdict.values(dict_2))
# dict_values([5, 6, 'empty key'])
print(defaultdict.items(dict_2))
# dict_items([
#   ('E', 5), ('F', 6), ('G', 'empty key')
# ])
print(defaultdict.get(dict_2, 'E'))
# 5

#################################################################################
#                                namedtuple                                     #
#################################################################################

test_tuple = (255, 'A', True)
print(test_tuple[1])
# A
# ---------------------------------------------------------------------------
Person = namedtuple('Person', ['name', 'high', 'weight'])
louis = Person('Louis', 1.82, 79)
print(louis.high)
print(louis.weight)
print(louis.name)
"""
    1.82
    79
    Louis
"""
print(louis[0])
print(louis[1])
print(louis[2])
"""
    Louis
    1.82
    79
"""

#################################################################################
#                                PRACTICE                                       #
#################################################################################

list_a = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
counter = Counter(list_a)
print(counter)
# Counter({5: 4, 2: 3, 1: 2, 3: 2, 6: 2, 7: 2, 4: 1})

my_dict = defaultdict(lambda: "Value not found")
my_dict['age'] = 44
print(my_dict['A'])
# Value not found

text_deque = 'qwertyuiop'
test_deque = deque(text_deque)
print(test_deque)
# deque([
#   'q', 'w', 'e', 'r', 't',
#   'y', 'u', 'i', 'o', 'p'
# ])

test_deque.append('j')  # add a new entry to the right side
test_deque.appendleft('f')  # add a new entry to the left side
print(test_deque)
# deque([
#   'f', 'q', 'w', 'e', 'r', 't',
#   'y', 'u', 'i', 'o', 'p', 'j'
# ])

test_deque.rotate(1)  # right rotation
print(test_deque)
# deque([
#   'j', 'f', 'q', 'w', 'e', 'r',
#   't', 'y', 'u', 'i', 'o', 'p'
# ])

test_deque.rotate(-1)  # left rotation
print(test_deque)
# deque([
#   'f', 'q', 'w', 'e', 'r', 't',
#   'y', 'u', 'i', 'o', 'p', 'j'
# ])


