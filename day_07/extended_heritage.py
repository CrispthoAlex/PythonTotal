class Animal:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def birth(self):
        print("This animal was born")

    def talk(self):
        print("This animal makes sounds")


class Bird(Animal):

    def __init__(self, age, color, high):
        """
        option 1. Animal heritage
        self.age = age
        self.color = color
        """
        # option 2. Animal heritage
        super().__init__(age, color)
        self.high = high

    # talk() method is heritage and overwrite from Animal class
    def talk(self):
        print("Twit, twit")

    def fly(self, meters):
        print(f"The bird flies {meters} meters")


# just need three args, age, color and high. Bird heritage
silvester = Bird(4, "Black", 60)
silvester.birth()
# talk method was overwriting
silvester.talk()
silvester.fly(20)

# just need two args, age and color. Animal heritage
new_animal = Animal(12, "gray")
new_animal.birth()
print("\n" * 2)

"""
Multiple heritage
"""


class Father:

    def talk(self):
        print("Hello")

    def toWork(self):
        print("Working at hospital")


class Mother:

    def laugh(self):
        print("Ha ha ha")

    def talk(self):
        print("What's going on?")

    def toWork(self):
        print("Working as prosecutor")


class Son(Father, Mother):
    pass


class Grandson(Son):
    pass


my_grandson = Grandson()
# Father heritage
my_grandson.talk()
# Mother heritage
my_grandson.laugh()
# talk method was heritage from Father class.
my_grandson.talk()
# Heritage order => first Father class, later Mother class
print(Grandson.__mro__)
"""
(<class '__main__.Grandson'>, <class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
"""


# Practice 1
class Daughter(Mother, Father):
    pass


melissa = Daughter()
melissa.toWork()  # Working as prosecutor


# Practice 2
class Vertebrate:
    vertebrate = True


class Bird(Vertebrate):

    itHasABeak = True

    def toLayEggs(self):
        print("Laying eggs")


class Reptile(Vertebrate):
    venomous = True


class Fish(Vertebrate):

    def swing(self):
        print("Swimming")

    def toLayEggs(self):
        print("Poniendo huevos")


class Mammal(Vertebrate):
    def walk(self):
        print("Walking")

    def suckle(self):
        print("suckling young")


class Platypus(Fish, Reptile, Bird, Mammal):
    pass


# practice 3
class FatherCls:
    eyes_color = "brown"
    hair_type = "curls"
    high = "medium"
    voice = "low"
    favorite_sport = "tennis"

    def laugh(self):
        return "Jajaja"

    def hobby(self):
        return "Paint wood in my free time"

    def walk(self):
        return "Walking with long and fast steps"


class SonClss(FatherCls):

    def hobby(self):
        return "I play video games in my free time"

