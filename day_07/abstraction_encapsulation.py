"""
Abstraction
It's related to hiding all the complexity  that something may have inside , offering an interface
with high-level functions, generally simple  to use, that can be used to interact with the object. application without having knowledge of what is inside.

"""


"""
Encapsulation
It's related to  hiding certain internal states of an object from the outside , such that it is  the same object that
accesses or modifies them , but that said action cannot be carried out from the outside. , calling the methods or
attributes directly.
"""


class Person:
    public_attribute = "Show"  # Accessible from outside
    __private_attribute = "Hidden"  # Not accessible

    # Not accessible from outside
    def __hidden_method(self):
        print("This method is hidden")
        self.__variable = 0
    
    # Accessible from outside
    def normal_method(self):
        # The method is accessible from the inside
        self.__hidden_method()


student = Person()
"""
This method is not accessible from the outside
student.__hidden_method()
Unresolved attribute reference '__hidden_method' for class 'Person'
"""
student.normal_method()  # This method is accessible
