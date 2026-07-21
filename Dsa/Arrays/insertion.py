#insertion and deletion insert adding a new element to an array
numbers = [10,20,30]
numbers.append(40)#adding element at last
print(numbers)

#deletion means removing an element from an array
numbers = [10,20,30,40]
numbers.remove(20)
print(numbers)

numbers = [5,15,25]
numbers.append(35)
numbers.remove(15)
print(numbers)

#pop by index Removes by index and returns the removed value.


numbers = [10,20,30]
x = numbers.pop(2)
print(x)
print(numbers)



numbers = [10,20,30]

del numbers[1]

print(numbers)

#array insertion element at specific position insert at beginning
numbers = [20,30,40]

numbers.insert(0,10)

print(numbers)

#insert at end 
numbers =[10,20,30]
numbers.insert(3,40)
print(numbers)

#append add at ending and insert add at any position
numbers = [5,10,20,25]
numbers.insert(2,15)
print(numbers)

numbers = [20,30,40]
numbers.insert(0,10)
print(numbers)

numbers = [10,20,30]
numbers.append(40)
print(numbers)

#Without using append(), add 50 at the end.
numbers = [10,20,30,40]
numbers.insert(len(numbers),50)
print(numbers)

#deletion by index using pop()

numbers = [10,20,30,40]
numbers.pop(1)
print(numbers)

numbers = [5,10,15,20]
del numbers[2]
print(numbers)

numbers = [100,200,300,400]

x = numbers.pop(3)
print(x)
print(numbers)
