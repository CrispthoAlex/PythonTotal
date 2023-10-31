class Bird:
    # class attribute
    flies = True

    # instance attribute
    def __init__(self, color, species):
        self.color = color
        self.species = species


my_bird = Bird("black", "Eagle")
print(f"My bird is a {my_bird.species} with {my_bird.color} color")
# My bird is a Eagle with black color
print(my_bird.flies)
# True
print(Bird.flies)
# True
