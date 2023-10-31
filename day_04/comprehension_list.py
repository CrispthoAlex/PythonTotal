lista_1 = list(range(2, 99))
for nb in lista_1:
    print(nb)

# comprehension list
list_com = [nb * 2 for nb in lista_1]
print(list_com)

word = "python"
word_list = []

for ltr in word:
    word_list.append(ltr)
print(word_list)  # ['p', 'y', 't', 'h', 'o', 'n']

# comprehension list
word_list1 = [ltr for ltr in word]
print(word_list1)  # ['p', 'y', 't', 'h', 'o', 'n']

# comprehension list adding conditional 1
list_com = [nb * 2 for nb in lista_1 if nb % 2 == 0]
print(list_com)
"""
[
    4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52,
    56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100,
    104, 108, 112, 116, 120, 124, 128, 132, 136, 140,
    144, 148, 152, 156, 160, 164, 168, 172, 176, 180,
    184, 188, 192, 196
]

"""
# comprehension list adding conditional 2
list_com = [nb * 2 if nb % 2 == 0 else "odd" for nb in lista_1]
print(list_com)
"""
[
    4, 'odd', 8, 'odd', 12, 'odd', 16, 'odd', 20, 'odd', 24,
    'odd', 28, 'odd', 32, 'odd', 36, 'odd', 40, 'odd', 44,
    'odd', 48, 'odd', 52, 'odd', 56, 'odd', 60, 'odd', 64,
    'odd', 68, 'odd', 72, 'odd', 76, 'odd', 80, 'odd', 84,
    'odd', 88, 'odd', 92, 'odd', 96, 'odd', 100, 'odd', 104,
    'odd', 108, 'odd', 112, 'odd', 116, 'odd', 120, 'odd', 124,
    'odd', 128, 'odd', 132, 'odd', 136, 'odd', 140, 'odd', 144,
    'odd', 148, 'odd', 152, 'odd', 156, 'odd', 160, 'odd', 164,
    'odd', 168, 'odd', 172, 'odd', 176, 'odd', 180, 'odd', 184,
    'odd', 188, 'odd', 192, 'odd', 196
]
"""