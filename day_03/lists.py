my_list = ["a", "b", "c"]
new_list = ["here", 10, 0.3333, True, {"key": "value"}]
extract_ele = my_list[2]
new_list2 = ["z", "t", "n", True, 3.1415232423]
list3 = new_list + new_list2

print(type(my_list))  # <class 'list'>
print(len(new_list))
print(extract_ele)
print(new_list[:3])
print(list3)
"""
<class 'list'>
5
c
['here', 10, 0.3333]
['here', 10, 0.3333, True, {'key': 'value'}, 'z', 't', 'n', True, 3.1415232423]
"""

list3[4] = "No dic"
print(list3)
new_list2.append(9.10)
print(new_list2)
new_list.pop()  # remove last element
print(new_list)
print(new_list2.pop(3))  # remove element on idx 3
print(new_list2)
"""
['here', 10, 0.3333, True, {'key': 'value'}, 'z', 't', 'n', True, 3.1415232423]
['here', 10, 0.3333, True, 'No dic', 'z', 't', 'n', True, 3.1415232423]
['z', 't', 'n', True, 3.1415232423, 9.1]
['here', 10, 0.3333, True]
True
['z', 't', 'n', 3.1415232423, 9.1]
"""

un_order_list = ["g", "m", "b", "x", "9"]
order_list = un_order_list.sort()
print(order_list)
print(un_order_list)
un_order_list.reverse()
print(un_order_list)
"""
None
['9', 'b', 'g', 'm', 'x']
['x', 'm', 'g', 'b', '9']
"""

redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]
print(redes.sort())
print(redes)
