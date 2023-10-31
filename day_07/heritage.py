# Heritage

class Animal:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def birth(self):
        print("This animal was born")


class Bird(Animal):
    pass


print(Animal.__subclasses__())
canary = Bird(4, 'red')
canary.birth()
print(canary.color)

