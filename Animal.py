class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight

    @property
    def name(self,name):
        self.name = name

    def make_noise(self):
        return "GRRRR"

    def __str__(self):
        return "{} is a {} and says {}".format(self.__name, type(self).__name__, self.make_noise())

    def __gt__(self, animal2):
        if self.__weight > animal2.__weight:
            return True
        else:
            return False

    # Other magic methods for classes
    # __eq__ : Equal
    # __ne__ : Not Equal
    # __lt__ : Less Than
    # __gt__ : Greater Than
    # __le__ : Less Than or Equal
    # __ge__ : Greater Than or Equal
    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : Multiplication
    # __div__ : Division
    # __mod__ : Modulus


class Dog(Animal):
    def __init__(self, name="unknown", owner="unknown", weight=0):
        Animal.__init__(self, name, weight)
        self.__owner = owner

    def __str__(self):
        return super().__str__() + " and is owned by " + self.__owner

animal = Animal("Spot", 100)
print(animal)
dog = Dog("Bowser", "Bob", 150)
print(dog)
print(animal > dog)




