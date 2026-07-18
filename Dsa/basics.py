# Definition: A data structure is a way of organizing and storing data so it can be used efficiently.
# Imagine you want to make tea.

'''
Steps:

Boil water.
Add tea powder.
Add milk.
Add sugar.
Serve.

These steps form an algorithm.'''

# Definition: An algorithm is a step-by-step procedure to solve a problem.

# Data Structure + Algorithm

# Think about Google Maps.

# Data Structure: Stores roads, cities, and distances.
# Algorithm: Finds the shortest route to your destination.

# Both work together

'''
Index:   0   1   2   3   4
Value:  10  20  30  40  50
'''

numbers = [10,20,30,40,50]


'''
Because arrays are used everywhere:

Student records
Shopping carts
Products
Messages
Photos
Scores

Almost every application stores collections of items.
'''

#basic operation using array

'''numbers = [10,20,30,40,50]
print(numbers[2])
#update an array
numbers[1] = 10
print(numbers)
#append an array
numbers.append(50)
print(numbers)
#remove method
numbers.remove(10)
print(numbers)
'''
'''
Most array questions are based on a few common patterns.

Find maximum
Find minimum
Find sum
Count elements
Search an element
Reverse an array
Find second largest
Remove duplicates
Rotate array
Two Sum
'''

numbers = [12,45,7,89,34]
largest = numbers[0]#start assuming first element is the largest.

for num in numbers:
    if num>largest:
        largest = num
print(largest)


# find the smallest number
numbers = [25,10,40,5,18]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)
'''
Time Complexity: O(n) (we visit each element once)
Space Complexity: O(1) (we use only one extra variable)
'''

#linear search
numbers = [10,25,40,60,80]
target = 40
found = False

for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Found")
else:
    print("not found")


numbers = [7, 15, 22, 18, 30]
target = 18

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        break


#challenge2
numbers = [10, 45, 23, 89, 67]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Largest:",largest)
print("Second Largest:",second)
