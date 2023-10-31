my_list = [1, 1, 1, 1, 1, 1, 1]
print(my_list, "\n", len(my_list))


class Object:
    pass


my_object = Object()
print(my_object)

"""
print(len(my_object))
    Traceback (most recent call last):
      File \"C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_07\\special_methods.py\", line 11, in <module>
        print(len(my_object))
              ^^^^^^^^^^^^^^
    TypeError: object of type 'Object' has no len()
"""


class CD:

    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):
        return (f"Album: {self.title}\n"
                f"Author: {self.author}")

    def __len__(self):
        return self.songs

    def __del__(self):
        print(f'Object has been deleted')


my_cd = CD('Pink Floyd', 'The wall', 24)
print(str(my_cd))
print(len(my_cd))
del my_cd


