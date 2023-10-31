text = "Testing text to Check String Methods"
str_len = len(text)  # char numbers

test1 = text.upper()
test2 = text[3].upper()
test3 = text.lower()
test4 = text[0].lower()
test5 = text.split()
test6 = text.split('t')
test7 = "_".join(test5)
test8 = "#".join(test6)
test9 = text.find("Ch")
test10 = text.find("z")
test11 = text.replace("e", "@")

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
print(test7)
print(test8)
print(test9)
print(test10)
print(test11)

"""""
TESTING TEXT TO CHECK STRING METHODS
T
testing text to check string methods
t
['Testing', 'text', 'to', 'Check', 'String', 'Methods']
['Tes', 'ing ', 'ex', ' ', 'o Check S', 'ring Me', 'hods']
Testing_text_to_Check_String_Methods
Tes#ing #ex# #o Check S#ring Me#hods
16
-1
T@sting t@xt to Ch@ck String M@thods
"""""

