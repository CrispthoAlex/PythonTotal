and_test = (4 < 5) and (5 > 6)
and_test1 = (4 < 5) and (5 == 2 + 3)
and_test2 = (55 < 55) and ("perro" == "perro")

print(and_test, and_test1, and_test2)
# False True False

or_test = 10.0 == 10 or 3 == 3.0
or_test1 = 10.0 == 100 or 3 == 3.0
or_test2 = 10.0 == 100 or 3 == 30.0

print(or_test, or_test1, or_test2)
# True True False

text = "Hello python, welcome home"
logic_test = ("python" in text) and ("home" in text)
logic_test1 = ("javascript" in text) and ("home" in text)
logic_test2 = "javascript" not in text
logic_test3 = not ("B" == "B")
logic_test4 = not ("B" != "B")

print(logic_test, logic_test1, logic_test2, logic_test3, logic_test4)
# True False True False True
