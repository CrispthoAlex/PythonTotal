# methods, help and documentation
dic = {
    "c1": 100, "c2": 200, "c3":50
}
a = dic.popitem()
# `popitem(self)` on docs.python.org
print(dic, a)
# {'c1': 100, 'c2': 200}
# ('c3', 50)

symbols = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
ch_removed = ",:%_#"
print(symbols.lstrip(ch_removed))
# Pyt%on_ _Total,,,,,,::#

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)
# ['mango', 'banana', 'cereza', 'naranja', 'ciruela', 'pomelo']

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
# false
