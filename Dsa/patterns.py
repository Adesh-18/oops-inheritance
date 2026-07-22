# a loop is a repeated block of code until a condition becomes false or until all items are processed
# print hello 5 times you dont wite print("hello ") five times you use a loop
# types of loops
# for variable in sequence:
#     #code

for i in range(5):#range gennerates up to 5 values
    print(i)

fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)

#use while loop when you dont know exactly how many times the loop should run it continues should run it continue as the condition is true
# while condition
#code

count = 1
while count<=5:
    print(count)
    count+=1#it is important without it the condition never changes,causing infinite loop

#range(5) produces 0 1 2 3 4
#range(2,6) produce 2 3 4 5 start where to begin and stop where to s
#range(1,10,2) produces 1 3 5 7 9 start wheere to begin stop where to stop step how much to increase
for i in range(1,11,2):
    print(i)

for x in range(5):
    print(x)

#loop controls statements
#breaks stops the loop immediately
for i in range(1,6):
    if i == 5:#stops the loop when it comes
        break
    print(i)

#break stops the loop immediately

for i in range(1,6):
    if i == 4:
        break#stops the loop immediately
    print(i)

#continue skips the current itteration and moves to the next one
for i in range(1,6):
    if i == 4:
        continue#skip the number 4 and move to next one
    print(i)

#pass does nothing it's used as a placeholder
for i in range(5):
    pass#does nothing 

# nested loops a loop inside another loop 
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
#when to use these loops 
# use for loops when the number of repetitions is known or you're iterating over sequence
# use while loop when the loop should continue until a condition changes

for r in range(1,11):
    print(r)

for i in range(2,11,2):#print only even numbers
    print(i)

for i in range(10,0,-1):#print in reverse order
    print(i)

for i in range(20,0,-2):
    print(i)#reverse order even numbers

#using for loops if condition
for num in range(1,11):
    if num % 2 == 0:#check condition and print even numbers
        print(num)
#odd numbers
for num in range(1,11):
    if num%2 !=0:# means not equal to
        print(num)

#print square of numbers
for num in range(1,6):
    print(num*num)#it num * num --> 2*2 = 4 
#another one
for num in range(1,6):
    print(num**2)#** means power


#print number and square
for num in range(1,6):
    print(num,num**2)

for number in range(1,20):
    print(number,number**2)

#sum of numbers
total = 0#startin with zero
for num in range(1,6):
    total+=num#assume 1 + 1 + 1 + 2 = 3 3 + 3 = 6
print(total)

total = 0
for num in range(1,5):
    total += num
print(total)

# find the largest number
numbers = [12,8,25,17,5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

total = 0

for i in range(1, 11):
    total += i

print(total)

#count even and odd numbers
numbers = [10,7,8,15,20,3]
even = 0
odd = 0
for num in numbers:
    if num %2 == 0:
        even += 1
    else:
        odd+=1
print("EVEN:",even)
print("Odd:",odd)

# find the smallest number
numbers = [12,45,7,89,23]
largest = numbers[0]
for num in numbers:
    if num >largest:
        largest = num
print(largest)

numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# reverse a string
text = "python"
for i in range(len(text)-1,-1,-1):
    print(text[i],end = "")

#multilication table of 5
for i in range(1,11):
    print("5 X",i,"=",5*i)

#print numbers from 50 to 1
for i in range(50,0,-1):
    print(i)

total = 0

for num in range(1, 101):
    if num % 2 != 0:
        total += num

print(total)

total = 0
for num in range(1,1001):
    if num % 2 !=0:
        total +=num

print(total)


#count vowels in a string
text = "programming"#vowels are a e i o u
count = 0
for ch in text:
    print(ch)
    if ch in "aeiou":
        count+=1
print(count)


#count consonants
#a consonants is any alphabet that is not a vowel
text = "programming"
count = 0
for ch in text:
    if ch not in  "aeiou":
        count +=1
print(count)

#sum of digits
# Suppose:

# Number = 4582

# You should find:

# 4 + 5 + 8 + 2 = 

num = 4582
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print(total)

#reverse a number
num = 4582
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num // 10
print(reverse)

# largest number
numbers = [12,45,7,89,23]
largest = numbers[0]
for num in numbers:
    if num> largest:
       largest = num

print(largest)

numbers = [12,45,7,89,23]
smallest = numbers[0]
for num in numbers:
    if num<smallest:
        smallest = num
print(smallest)

#second largest

numbers = [12,45,7,89,23]
largest = numbers[0]
second =  0

for num in numbers:
    if num > largest:
       second = largest
       largest = num
    elif num > second and num != largest:
        second = num
print("Largest:",largest)
print("Second largest:",second)


#factorial of number
# num = 5
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)

# num = 7
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

# num = 4
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

#prime number
# a number has only two factors 1 and number itself
num = 7
for i in range(2,num):
    if num % i ==0:
        print(i)


num = 8

for i in range(2, num):
    if num % i == 0:
        print(i)

num = 7
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not Prime")

num = 9
is_prime = True
for i in range(2,num):
    if num % i == 0:
        is_prime = False
if is_prime:
    print("Prime")
else:
    print("Not Prime")

num = 11

for i in range(2, num):
    if num % i == 0:
        print(i)

num = 12

for i in range(2, num):
    if num % i == 0:
        print(i)

num = 12
is_prime = True
for i in range(2,num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("not a prime")

numbers = [12,7,18,30,41]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even",even)
print("Odd:",odd)


numbers = [12,7,18,30,41]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)

numbers = [12,7,18,30,41]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)

numbers = [12,7,18,30,41]
total = 0
for num in numbers:
    total += num
print(total)

#find average of numbers
numbers = [12,7,18,30,41]
total = 0
for num in numbers:
    total+= num
average = total/len(numbers)

print(average)

#second largest number
numbers = [12,7,18,30,41]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num!= largest:
        second = num
print("Largest:",largest)
print("Second:",second)


#second smallest number
numbers = [12,7,18,30,41]
smallest = numbers[0]
second = numbers[0]
for num in numbers:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num
print("Smallest:",smallest)
print("Second Smallest:",second)

#reverse a list
numbers = [10,20,30,40,50]
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])

#find the maximium and minimum in one loop
numbers = [15,8,23,4,19]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

#count positive and negative numbers
numbers = [10,-5,20,-8,0,15,-2]
positive = 0
negative = 0
zero = 0
for num in numbers:
    if num>0:
        positive +=1
    elif num<0:
        negative +=1
    else:
        zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)



numbers = [1,2,3,-1,-2,-3,0]
positive = 0
negative = 0
zero = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("positive:",positive)
print("negative:",negative)
print("zero:",zero)


#count vowels and consonants in a string
text = "python"
vowels = 0
consonants = 0
for ch in text:
    if ch in "aeiou":
        vowels += 1
    else:
        consonants +=1
print("vowels count:",vowels)
print("Consonants:",consonants)


def greet():
    print("Hello")

print("Start")
greet()
print("End")


def greet():
    print("Welcome to python")
greet()

# function with parameter
def greet(name):
    print("Hello:",name)
greet("adesh")

# function with return value
def add(a,b):
    return a + b
result = add(10,20)
print(result)


def add (a,b):
    return a + b
adds = add(5,7)
print(adds)


def add (a,b):
    return a + b
x = add(10,20)
y = x * 2

print(y)

# square of a number using return
def square(a):
    return a*a

x = square(6)
print(x)

#cube of a number
def cube(a):
    return a ** 3
x = cube(3)
print(x)

# a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)

#default parameters
def greet(name = "Guest"):
    print("Hello",name)
greet()
greet("Adesh")

# dictionary
# student = {
#     "Name":"Adesh",
#     "Age": 21,
#     "Branch":"Cse"
# }

# print(student["Name"])
# print(student["Age"])
# print(student["Branch"])
# #add new value to it
# # student["Age"] = "22"
# student["city"] = "Vizag"
# print(student["city"])

#challenge 2
# student = {
#     "Name": "Adesh",
#     "Age": 21,
#     "City": "Vizag"
# }
# student["Age"] = "22"
# student["City"] = "Hyderbad"
# for i in student:
#     print(i, ":", student[i])
# for i in student:
#     print(student[i])#student[i] gets the corresponding value.


# student = {
#     "Name": "Adesh",
#     "Age": 22,
#     "City": "Hyderabad"
# }
# for i in student:
#     print(i,":",student[i])

#items
student = {
    "Name": "Adesh",
    "Age": 22,
    "City": "Hyderabad"
}
for key,value in student.items():
    print(key,":",value)

student = {
    "Name": "Adesh",
    "Age": 22,
    "City": "Hyderabad"
}
print(student.keys())
print(student.values())
print(student.items())

student = {
    "Name": "Adesh",
    "Age": 22,
    "City": "Hyderabad"
}
print(student.get('Name'))
print(student.get("Phone"))
print(student.get("phone","Not found"))


student = {
    "Name": "Adesh",
    "Age": 22,
    "City": "Hyderabad"
}

print(student.get("Name"))
print(student.get("City"))
print(student.get("College"))
print(student.get("College", "QIS not found"))


#removing items from dictionary
#pop() POPITEM() clear()
student = {
    "Name": "Adesh",
    "Age": 22,
    "City": "Hyderabad"
}

student.pop("Age")#It removes a specific key from the dictionary.

print(student)


