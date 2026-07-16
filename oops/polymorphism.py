#polymorphism means same method name , different behaivour

# POLY = Many
# MORPH = Forms

# Polymorphism = Many Forms

class Dog:
    def sound(self):
        print("Dog braks")
class Cat:
    def sound(self):
      print("cat meows")
d1 = Dog()
c1 = Cat()
d1.sound()
c1.sound()

# sound()
# Dog.sound() → Bark
# Cat.sound() → Meow
# Cow.sound() → Moo

#Same method name, different behavior.
class python:
    def language(self):
        print("Python language")
class Java:
    def language(self):
        print("java language")
p = python()
j = Java()
p.language()
j.language()

#example 2
class Dog():
    def sound(self):
        print("Bark")
class cat:
    def sound(self):
        print("meow")
class cow:
    def sound(self):
        print("moo")
animals = [Dog(),Cat(),cow()]
for animal in animals:
    animal.sound()

# Same method call works differently for different objects