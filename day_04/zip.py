names = ["Laura", "Luis", "Felipe", "Carolina", "Maria"]
ages = [14, 16, 15, 13]
cities = ["Cali", "Brasilia", "Guayaquil"]

combine = zip(names, ages, cities)
print(combine)
# <zip object at 0x000001B42C0D5F40>

combine = list(combine)
print(combine)
"""
[
    ('Laura', 14, 'Cali'),
    ('Luis', 16, 'Brasilia'),
    ('Felipe', 15, 'Guayaquil')
]
"""

for name, age, city in combine:
    print(
        f"{name} is {age} years old, and live in {city}"
    )
"""
Laura is 14 years old, and live in Cali
Luis is 16 years old, and live in Brasilia
Felipe is 15 years old, and live in Guayaquil
"""
