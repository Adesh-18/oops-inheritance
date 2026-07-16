# Difference Between Encapsulation and Abstraction

# This is a common interview question.

# Encapsulation	Abstraction
# Protects data	Hides complexity
# Uses private variables (__)	Shows only necessary features
# Focus: Data security	Focus: Simplicity
# Encapsulation

# "Protect my data."

# Abstraction

# "Hide unnecessary details."
# Encapsulation protects important data by restricting direct access and allowing controlled access through methods.
# Abstraction hides unnecessary implementation details and shows only the features that the user needs.

# inheritance	Reuse code from a parent class.
# Polymorphism	Same method name, different behavior.
# Encapsulation	Protect data using controlled access.
# Abstraction	Hide implementation details and show only essential features.

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
class Tesla(Car):
    def start(self):
        print("Tesla Started")
car = Tesla()
car.start()

# This means:

# Every child class must create its own start() method.

# The parent only says:

# "There must be a method called start()."

# It doesn't say how to start.
from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
class pulsar(Bike):
    def start(self):
        print("pulsar started")
bike = pulsar()
bike.start()

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("bark")
dog = Dog()
dog.sound()