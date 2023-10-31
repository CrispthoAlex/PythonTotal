dictionary1 = {"v1": 1, "v2": 2, "v3": 3}

print(dictionary1)
print(type(dictionary1))
"""
{'v1': 1, 'v2': 2, 'v3': 3}
<class 'dict'>
"""
client = {
    "nombre": "juan",
    "apellido": "Solano",
    "peso": 35,
    "edad": 10,
    "altura": 1.45,
}
print(client["nombre"])  # juan

dicc = {
    "k1": [1, 2, 3, 4, 5, 6],
    "k2": "miami fc",
    "k3": "polly pocket stadium",
    "k4": {
        "ruta": "M39",
        "llegada": "8:00",
        "salida": "15:00",
        "tikect": 3000
    },
    "k5": ["t", "u", "v", "x", "y"]
}
print(dicc["k5"][2].upper())  # V
dicc["k6"] = {"Home": True, "Visit": False}
print(dicc["k6"])  # {'Home': True, 'Visit': False}

dicc["k2"] = dicc["k2"].upper()
print(dicc["k2"])  # MIAMI FC

print(dicc.keys())
# dict_keys(['k1', 'k2', 'k3', 'k4', 'k5', 'k6'])

print(dicc.values())
"""
dict_values([
    [1, 2, 3, 4, 5, 6],
    'MIAMI FC',
    'polly pocket stadium',
    {'ruta': 'M39', 'llegada': '8:00', 'salida': '15:00', 'tikect': 3000},
    ['t', 'u', 'v', 'x', 'y'], {'Home': True, 'Visit': False}
])
"""

print(dicc.items())
"""
dict_items([
    ('k1', [1, 2, 3, 4, 5, 6]),
    ('k2', 'MIAMI FC'),
    ('k3', 'polly pocket stadium'),
    ('k4', {'ruta': 'M39', 'llegada': '8:00', 'salida': '15:00', 'tikect': 3000}),
    ('k5', ['t', 'u', 'v', 'x', 'y']),
    ('k6', {'Home': True, 'Visit': False})
])
"""