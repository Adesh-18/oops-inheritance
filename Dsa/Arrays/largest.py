# Find the largest element
# keep one variable largest
# compare every element
arr = [5,8,2,10,3]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(largest)


arr = [5,8,4,9,10]
smallest = arr[0]
for num in arr:
    if num < smallest:
        smallest = num
print(smallest)