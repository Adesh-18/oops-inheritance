arr = [5,10,15,20]
total = 0
for num in arr:
    total += num
print(total)

#practicing array access update traverse search maximium minimum sum
#accessing element
arr =[1,2,3,4,5]
print(arr[0])
print(arr[2])
print(arr[1])

#updaring
arr[1] = 22
print(arr[1])

#traverse
for num in arr:
    print(num)
#search
target = 22
found = False
for num in arr:
    if num == target:
        found = True
        break
print(found)    

#find maximium
maximium = arr[0]
for num in arr:
    if num > maximium:
        maximium = num
print(maximium)

# minimum
minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
print(minimum)
#sum of array
total = 0

for num in arr:
    total += num
print(total)

# Operation	Complexity
# Access	O(1)
# Update	O(1)
# Traverse	O(n)
# Search	O(n)
# Maximum	O(n)
# Minimum	O(n)
# Sum	O(n)
