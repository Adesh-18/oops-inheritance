'''
two sum
suppose you have a list of numbers
numbers = [4,6,9,12]
and someone  gives you a target
targest = 15
Your task is:

Find two numbers whose sum equals the target.

lets understand 
think of your four friends standing in a line
2    7    11    15
Can you find any two friends whose total is 9?"
9-2 = 7
is 7 is the array
2+7 = 9
'''



numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Indices:", i, j)
            print("Values:", numbers[i], numbers[j])