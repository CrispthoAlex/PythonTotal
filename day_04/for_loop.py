names = ["maria", "luis", "ana", "Jade", "Xavier"]

for name in names:
    order_list = names.index(name) + 1
    print(f"Hi {name}, you're student {order_list}")
"""
    Hi maria, you're student 1
    Hi luis, you're student 2
    Hi ana, you're student 3
    Hi Jade, you're student 4
    Hi Xavier, you're student 5
"""

for name in names:
    if name.startswith("l"):
        print(f"Hi {name}, you're chosen student")
"""
    Hi luis, you're chosen student
"""

numbers = range(12)
value = 0

for nb in numbers:
    print(f"value {value} + {nb}")
    value += nb
    print(f"partial result = {value}")

print("\nThis is the final value", value)
"""
value 0 + 0
partial result = 0
value 0 + 1
partial result = 1
value 1 + 2
partial result = 3
value 3 + 3
partial result = 6
value 6 + 4
partial result = 10
value 10 + 5
partial result = 15
value 15 + 6
partial result = 21
value 21 + 7
partial result = 28
value 28 + 8
partial result = 36
value 36 + 9
partial result = 45
value 45 + 10
partial result = 55
value 55 + 11
partial result = 66

This is the final value 66
"""
word = "python"
for ltr in word:
    print(ltr)

for nb in tuple(range(5)):
    print(nb)

for n1,n2 in [[1, 2], [3, 4], [5, 6], [7, 8]]:
    # print(n1, n2)
    print(n2)

dic_abc = {
    "ltr1": "a",
    "ltr2": "b",
    "ltr3": "c",
    "ltr4": "d",
}

for key, value in dic_abc.items():
    # print(item)
    print(key, value)

for item in dic_abc.items():
    print(item)

for value in dic_abc.values():
    print(value)

name = input("Type your name: ")

for ltr in name:
    if ltr == "r":
        # break
        continue
    print(ltr)

