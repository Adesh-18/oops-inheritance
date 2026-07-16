#single inheritance
#multiplie inheritance
#multilevel inheritance
#hierarchical inheritance
#Hybrid inheritance

#single inheritance
'''
class Animal:
    def eat(self):
        print("animal is eating")
class Dog(Animal):
    def bark(self):
        print('Dog is barking')
d1 = Dog()
d1.eat()
d1.bark()
'''

#multilevel inheritance
'''
Grandparent
    ↓
Parent
    ↓
Child
'''
'''class Grandfather:
    def house(self):
        print("Grandfather's house")
class Father(Grandfather):
    def car(self):
        print("Father's car")
class son(Father):
    def bike(self):
        print("son's bike")
s1 = son()
s1.house()
s1.car()
s1.house()'''

'''
Grandfather
└── house()
      ↓
Father
├── house()  inherited
└── car()
      ↓
Son
├── house()  inherited
├── car()    inherited
└── bike()   own method
'''

# multiple inheritance
# one child inherits from more than one parent
'''
class Father:
    def car(self):
        print("Father's car")
class mother:
    def house(self):
        print("mother's home")
class child(Father,mother):#he child inherits from both classes.
    def bike(self):
        print("his bike")
c1 = child()
c1.car()
c1.house()
c1.bike()
'''

'''
class Python:
    def python_skill(self):
        print("i know python")
class Java:
    def java_skill(self):
        print("i know java")
class Developer(Python,Java):
    def web_skill(self):
        print("I know web developement")
d1 = Developer()
d1.python_skill()
d1.java_skill()
d1.web_skill()
'''


#Hierarchical Inheritance
# one parent -> multiple children
#        Parent
#        /    \
#       /      \
#    Child1   Child2

class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
class Cat(Animal):
    def meow(self):
        print("meowing")
d1 = Dog()
c1 = Cat()
d1.eat()
d1.bark()
c1.eat()
c1.meow()
#dog inherits from animal
#cat also inherit from the animal


#practice
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def code(self):
        print("Developer is coding")
class Tester(Employee):
    def test(self):
        print("Tester is testing")
d1 = Developer()
t1 = Tester()
d1.work()
d1.code()
t1.work()
t1.test()

# 1. Single
#    A → B

# 2. Multilevel
#    A → B → C

# 3. Multiple
#    A   B
#     \ /
#      C

# 4. Hierarchical
#       A
#      / \
#     B   C

# hybrid inheritance

#hybrid inheritance is a combination of two more inheritance types
    #     A
    #   / \
    #  B   C
    #   \ /
    #    D
class A:
    def method_a(self):
        print("A")
class B(A):
    def method_b(self):
        print("B")
class C(A):
    def method_c(self):
        print("C")
class D(B,C):
    def method_d(self):
        print("D")

d1 = D()
d1.method_a()
d1.method_b()
d1.method_c()
d1.method_d()

#it combines hierarchical inheritance: A --> B and A --> C
# multiple inheritance: D inherits from B and C

