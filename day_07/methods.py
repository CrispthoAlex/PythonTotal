class Bird:
    # class attribute
    flies = True

    # instance attribute
    def __init__(self, color, species):
        self.color = color
        self.species = species

    def chirp(self):
        print('pio pio, my color is {}'.format(self.color))

    def fly(self, metros):
        print(f"The bird has flown {metros} meters")


silvester = Bird('yellow', 'canary')
silvester.chirp()

silvester.fly(35)


class Alarma:

    def postpon(self, nb_minutes):
        print(f"The alarm has been postponed {nb_minutes} minutes")


clock_follow = Alarma()

clock_follow.postpon(30)


class Magician:

    def cast_spell(self):
        print("¡Abracadabra!")


merlin = Magician()

merlin.cast_spell()


class Dog:

    def bark(self):
        print("Guau!")


doggy = Dog()

doggy.bark()

