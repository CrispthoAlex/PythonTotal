"""
    Coupling is a concept that measures the dependency between
    two different modules ( such as classes)
"""
"""
    Weak coupling
    which implies that there is no dependency between one module and others.
    This is the ideal situation.
"""


# Example


class PetWeak:
    has_legs = True
    pass


class DogWeak:

    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print(f"The speed is {self.speed}")


my_pet_w = DogWeak("fast")
my_pet_w.run()
print(my_pet_w.speed)


"""
    Strong coupling
    Which is the opposite situation, and indicates that the module has internal 
    dependencies on others.
"""
# Example


class PetStrong:
    has_legs = True
    pass


class DogStrong:

    def run(self, speed):
        # it depends on Pet class
        if PetStrong.has_legs:
            self.speed = speed


my_pet_s = DogStrong()
my_pet_s.run("fast")
print(my_pet_s.speed)

