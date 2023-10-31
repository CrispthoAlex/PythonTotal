x = 63
y = 34
z = 7

print(f"{x} add {y} equal to {x + y}")
print(f"{x} minus {y} equal to {x - y}")
print(f"{x} times {y} equal to {x * y}")
print(f"{x} divided by {y} equal to {x / y}")
print()

print(f"{x} divided by {y} equal to {x // y} integer")
print(f"{x} modulated by {y} equal to {x % y}")
print(f"{x//9} power to {z} equal to {(x//9)**z}")
print(f"square root {x} equal to {x**(1/2)}")
print()

# Round values
value = x/y
round_value = round(value, 3)
round_value2 = round(value)
print(value, round_value, round_value2)
print(type(round_value), type(round_value2))

# test
print(round_value2, int(value))
num1 = round(13/2, 0)
print(num1, type(num1))
