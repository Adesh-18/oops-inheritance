# Print all elements of an array.
# Find the sum of all elements.
# Find the largest element.
# Find the smallest element.
# Count even and odd numbers.
# Count positive and negative numbers.
# Search for a given element.
# Print the array in reverse order.
# Find the average of the array.
# Count how many times a given number appears.
arr = [10,20,30,40,50]
for num in arr:
    print(num)
total = 0
for num in arr:
    total += num
print(total)

maximium = arr[0]
for num in arr:
    if num > maximium:
        maximium = num
print(maximium)

minimum = arr[0]
for num in arr:
    if num < minimum:
        minimum = num
print(minimum)

even = 0
odd = 0
for num in arr:
    if num % 2 == 0:
        even +=1
    else:
        odd +=1
print(even)
print(odd)

positive = 0
negative = 0
    
for num in arr:
    if num > 0:
        positive +=1
    elif num <0:
        negative += 1
    else:
        zero += 1
        
print(positive)
print(negative)

target = 20
found = False
for num in arr:
    if num == target:
        found = True
        break
print(found)

arr = [10,20,30,40,50]
total_sum = 0
for num in arr:
    total_sum += num
average = total_sum/len(arr)
print(average)
    
arr = [4, 2, 7, 4, 9, 4, 1]
target = 4
count = 0
for num in arr:
    if num == target:
        count+=1
print(count)

arr = [10,20,30,40,50]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])