arr = [5,10,8,20,15]
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)

# second largest element
arr = [4, 7, 1, 9, 6]
largest = second =  float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif second > largest and second != largest:
        second = num
print(largest)