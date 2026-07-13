#method overriding means were a child class changes the behaivour of a method inherited from its parent
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog  barks")#child class changed the behaivour of a method inherited from its children
d1 = Dog()
d1.sound()

# Both class have methods 
#     but d1 is a Dog object so python uses the Dog version
# Animal
# └── sound() → "Animal makes a sound"
#        ↓ inherited

# Dog
# └── sound() → "Dog barks"  ← overrides parent

# what if the child does not override
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


d1 = Dog()
d1.sound()

#with overridding
class Animal:
    def sound(self):
        print("animal makes a sound")
class Cat(Animal):
    def sound(self):
        print("cat sounds meow")
c1 =Cat()
c1.sound()


#real example
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is writing code")
class Tester(Employee):
    def work(self):
        print("tester testing software")

t1 = Tester()
d1 = Developer()
c1 = Employee()
t1.work()
c1.work()
d1.work()

#calling the parents overridden method
#sometime we want both parent method and child method
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        super().sound()#calls the parent's sound() method.super().__init__() this is called parents call
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        super().sound()
        print("cat is sounding meoww")
d1 = Dog()
c1 = Cat()
d1.sound()
c1.sound()
'''
Parent method: sound()
Child method:  sound()

Same method name
        ↓
Child version replaces parent version
        ↓
METHOD OVERRIDING'''