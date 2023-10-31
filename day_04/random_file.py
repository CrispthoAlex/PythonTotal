from random import *

value_rand_int = randint(1, 100)
# 22
value_random_uniform = uniform(1, 10)
# 7.84072494882795
value_rand = random()  # 0 between, and 1
# 0.7269349501853455
print(value_rand_int, round(value_random_uniform, 1), value_rand)
# 73 7.5

colors = ["blue", "red", "yellow", "black", "green", "pink"]
rand_color = choice(colors)
print(rand_color)
# black

numbers = list(range(0, 251, 5))
shuffle(numbers)  # on site
print(numbers)



