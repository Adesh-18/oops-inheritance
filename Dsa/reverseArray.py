#reverse using slicing
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

numbers = [5,15,25,35,45]
reverse = []
for i in range(len(numbers)-1,-1,-1):
    reverse.append(numbers[i])
print(reverse)