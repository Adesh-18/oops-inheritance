
'''Find:
Count Even and Odd Numbers

Number of even elements
Number of odd elements'''
numbers = [10,15,22,17,8,9]
#step1 creating variables
even = 0
odd = 0
#step 2 loop through array
for num in numbers:#step3 check if the number is even
    if num % 2 == 0:
        even += 1#increase even count
    else:
        odd += 1
print("Even:",even)
print("Odd:",odd)
'''
Time Complexity
O(n)

Because we visit each element once.

Space Complexity
O(1)

Only two variables (even and odd) are used.
'''

numbers = [12,7,18,30,41]
Even = 0
odd = 0
for num in numbers:
    if num %2 == 0:
        Even += 1
    else:
        odd += 1
print("Even count:",Even)
print("Odd count:",odd)

#challenge calculate sum of even numbers and odd numbers
numbers = [12, 7, 18, 30, 41]
even = 0
odd = 0
Even_Sum = 0
Odd_Sum = 0
for num in numbers:
    if num % 2 == 0:
      even +=1
      Even_Sum += num
    else:
        odd +=1
        Odd_Sum += num
print("Even Count:",even)
print("Odd Count:",odd)
print("Even Sum:",Even_Sum)
print("Odd Sum:",Odd_Sum)

'''
Time Complexity

Suppose there are 5 numbers.

The first number checks with 4 others.

The second checks with 3 others.

The third checks with 2 others.

The fourth checks with 1 other.

4 + 3 + 2 + 1

This grows roughly as:

O(n²)

So the brute-force solution is slow for large arrays.
'''


