name = "Adesh"
print(len(name))
# How does len() know the length of the string?

# Because Python internally calls a special method.
# name.__len__()
# You don't write it yourself.

# Python calls it automatically.

# These special methods are called Magic Methods (or Dunder Methods because they have double underscores).

class Student:
    pass
student = Student()
print(student)

# Wouldn't it be better if it printed:

# Student: Adesh

# Magic methods let you customize how your objects behave.
# without str
class Student:
    def __init__(self,name):
        self.name = name
student1 = Student("Adesh")
print(student1)

# with str
class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
student = Student("adesh")
print(student)


class Car:
    def __init__(self,brand):
        self.brand = brand
    def __str__(self):
        return "car Brand:" + self.brand
car = Car("Audi")
print(car)

# What is a magic method?

# # A magic method is a special method with double underscores that Python calls automatically to provide built-in behavior for object
# Why is __str__() used?

# It defines how an object should be displayed when printed.

class title:
    def __init__(self,book):
        self.book = book
    def __str__(self):
        return "Book:"+ self.book
book = title("Python")
print(book)

class Student1:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student:{self.name} Marks:{self.marks}"
stud = Student1("Adesh",95)
print(stud)


class Book:
    def __init__(self, title):
        self.title = title

    def __len__(self):
        return len(self.title)

book = Book("Python")

print(len(book))

#add magic method

# class Students:
#     def __init__(self,marks):
#         self.marks=  marks
# s1 = Students(90)
# s2 = Students(95)
# print(s1 + s2)
# TypeError: unsupported operand type(s) for +
# Because Python doesn't know how to add two Student objects.

class Student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = Student(90)
s2 = Student(95)

print(s1 + s2)