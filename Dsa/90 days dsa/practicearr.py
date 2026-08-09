#array problems
# traverse - go through elements
# compare - min , max, greater
# Rearrange - move,swap
#count - how many times an element occurs
#track state - max so far, index etc
# find maximium of an array
arr = [2,3,4,5]
max_value = arr[0]
for num in arr:
    if num > max_value:
        max_value = num
print("Maximum value:", max_value)

#compare minimium value

arr = [2,3,4,5]
min_value = arr[0]
for num in arr:
    if num< min_value:
        min_value = num
print("Minimum value:", min_value)

# find the second largest value in an array
arr = [2,3,4,5]
largest = arr[0]
second_largest = float('-inf')  # Initialize to negative infinity
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest value:", second_largest)

#reverse an array
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) -1
while left < right:
    arr[left],arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed array:", arr)

arr = [1, 2, 3,0, 4, 5,0]
left = 0
right = len(arr) -1
while left < right:
    if arr[left] == 0 and arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    elif arr[left] != 0:
        left += 1
    elif arr[right] == 0:
        right -= 1
print("Array with zeros moved to the end:", arr)

