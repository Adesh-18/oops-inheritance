arr = [5,9,2,11,7]
maximium = arr[0]

for num in arr:
    if num > maximium:
        maximium = num
print(maximium)

#time complexity 0(n)

arr = [10,20,20,30,40,50]
maximium = arr[0]
for num in arr:
    if num > maximium:
        maximium= num
print(maximium)

#Find minimum 

arr = [5,8,2,11,7]
minimum = [5,9,2,11,7]
minimum = arr[0]
for num in arr:
    if num < minimum:
        minimum = num
print(minimum)