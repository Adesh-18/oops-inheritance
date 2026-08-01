# 1. Reverse Array (Two Pointers) ⭐⭐⭐⭐⭐

# Learn one of the most important techniques in DSA.

# 2. Second Largest Element ⭐⭐⭐⭐⭐

# Asked by Amazon, Microsoft, Adobe, Oracle, Walmart, and many others.

# 3. Move All Zeroes to the End ⭐⭐⭐⭐⭐

# Very common interview problem.

# 4. Remove Duplicates from a Sorted Array ⭐⭐⭐⭐
# 5. Left Rotate Array ⭐⭐⭐⭐
# # 6. Right Rotate Array ⭐⭐⭐⭐

#Find the Second Largest Element
arr = [12,35,1,10,34,1]
largest = arr[0]
second = float("-inf")
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(largest)
print(second)

# Move All Zeroes to the End
#Move all the 0s to the end while keeping the order of the other numbers the same.
arr = [0,1,0,3,12]
position = 0
for i in range(len(arr)):
   if arr[i] != 0:
       arr[position] = arr[i]
       position += 1
while position < len(arr):
    arr[position] = 0
    position += 1
print(arr)

arr = [0, 0, 5, 0, 8]
position = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[position] = arr[i]
        position += 1
while position < len(arr):
    arr[position] = 0
    position += 1
print(arr)
        