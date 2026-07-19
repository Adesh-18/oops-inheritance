#reverse using slicing Reversing an array means arranging its elements in the opposite order.
numbers = [10,20,30,40,50]
reverse = numbers[::-1]
print(reverse)


#method 2
numbers = [10,20,30,40,50]
reverse = []
for i in range(len(numbers)-1,-1,-1):#range(start,stop,step)
    reverse.append(numbers[i])
print(reverse)


numbers = [10,30,50,60,80]
reverse = []
for i in range(len(numbers)-1,-1,-1):
    reverse.append(numbers[i])
print(reverse)
# The first element becomes the last, the last becomes the first, and so on.

# Reversing arrays is used in many real-world applications:

# Displaying data in reverse chronological order (latest messages first)
# Undo operations
# Palindrome checking
# String reversal
# Rotating arrays
# Many coding interview problems




# Start from the last index of the original array and keep adding elements to a new array.

#method 2 reverse in place (two pointers)
#instead of creTING ANOTHER  list we swap the first and last element then move in ward
# Swap first and last:

# [50, 20, 30, 40, 10]

# Swap second and second-last:

# [50, 40, 30, 20, 10]
'''
Interview Questions
1. What is array reversal?

Changing the order of elements so the first element becomes the last and the last element becomes the first.

2. Why do we use range(len(numbers)-1, -1, -1)?

To traverse the array from the last index to the first index.

3. Which method is better?
Using a new list: Easier to understand but uses extra memory (O(n) space).
Two pointers: More efficient because it reverses the array in place using only O(1) extra space. This is the approach interviewers often prefer.

Understanding why the loop starts at the last index and moves backward is the key idea behind reversing an array. Once that concept is clear, the code becomes much easier to remember.'''