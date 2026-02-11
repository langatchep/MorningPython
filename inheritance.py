
#Parent Class /Super Class/Base Class
class Animal:
    isMammal = True
    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")

#Child Class /Sub Class /Derived Class
class Cat(Animal):
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

    def move(self):
        print("Animal is moving")


class Horse:
    def neigh(self):
        hasTail = True
        print("Horse is neighing")

a = Animal()
c = Cat()
h = Horse()