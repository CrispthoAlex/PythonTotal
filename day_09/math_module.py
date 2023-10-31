import math

num = 321.8766456
result = math.floor(num)
print(result)
# 321
result = math.ceil(num)
print(result)
# 322
print(math.pi)
# 3.141592653589793
result = math.log(10000, 10)
print(result)
# 4.0
result = math.tan(550)
print(result)
# 0.22496972059380282
result = math.cos(90)
print(result)
# -0.4480736161291701

# --------------------------------------------------------------------
result = math.log10(25)
print(result)
# 1.3979400086720377
result = math.sqrt(math.pi)
print(result)
# 1.7724538509055159
result = math.factorial(7)
print(result)
# 5040
result = [(x, math.factorial(x)) for x in range(0, 8)]
print(result)
# [1, 1, 2, 6, 24, 120, 720, 5040]

