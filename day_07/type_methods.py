# methods type
"""instance methods
- access and modify the object attributes
- access to other methods
- modify the class state
"""
"""class methods

"""


# static methods
class Bird:
    # class attribute
    flies = True

    # instance attribute
    def __init__(self, color, species):
        self.color = color
        self.species = species

    # instance methods
    def chirp(self):
        print('pio pio')

    # instance methods
    def fly(self, metros):
        print(f"The bird has flown {metros} meters")
        self.chirp()

    # instance methods
    def black_painting(self):
        self.color = 'black'
        print(f"Now, bird is {self.color}")

    @classmethod  # decorator
    def put_eggs(cls, nb_eggs):
        print(f"Puts {nb_eggs} eggs")
        cls.flies = False
        print(cls.flies)

    @staticmethod
    def look():
        print("The bird looks")


# instance methods example
silvester = Bird('yellow', 'canary')
silvester.chirp()
silvester.fly(35)
silvester.black_painting()
silvester.flies = False
print(silvester.flies)

# class methods example
Bird.put_eggs(5)
"""Bird.fly(10)
TypeError: Bird.fly() missing 1 required positional argument: 'metros'
Note: fly method just for instances
"""

# static methods example
Bird.look()


class Pet:

    @staticmethod
    def breath():
        print("Inhalar... Exhalar")


Pet.breath()


class Player:
    life = False

    @classmethod
    def revive(cls):
        cls.life = True


class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
