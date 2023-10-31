class Cow:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + " says muuuu")


class Sheep:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + " says beeee")


cow1 = Cow("Linda")
sheep1 = Sheep("Tarciza")

cow1.talk()
# Linda says muuuu
sheep1.talk()
# Tarciza says beeee

# let's iterate
animals = [cow1, sheep1]

for animal in animals:
    print("Loop =>", animal.name)
    animal.talk()


def animal_talk(animal):
    print("animal_talk =>", animal.name)
    animal.talk()


animal_talk(cow1)
animal_talk(sheep1)


# practice 1

word = "polimorfismo"
list_a = ["Clases", "POO", "Polimorfismo"]
tuple_a = (1, 2, 3, 80)


def show_iterates_len(iterating):
    for ite in iterating:
        print(len(ite))


show_iterates_len([word, list_a, tuple_a])

# practice 2


class Magician:
    def atack(self):
        print("Ataque mágico")

    def defense(self):
        print("Escudo mágico")


class Archer:
    def atack(self):
        print("Lanzamiento de flecha")

    def defense(self):
        print("Esconderse")


class Samurai:
    def atack(self):
        print("Ataque con katana")

    def defense(self):
        print("Bloqueo")


merlin = Magician()
robin_hood = Archer()
last_samurai = Samurai()

warriors = [robin_hood, merlin, last_samurai]

for act in warriors:
    act.atack()


def warrior_defense(warrior):
    warrior.defense()


warrior_defense(merlin)
