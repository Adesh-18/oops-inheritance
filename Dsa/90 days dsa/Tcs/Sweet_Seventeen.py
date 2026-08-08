#Given a maximum of four digits to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as
# input, output its decimal value.
# num = input()
# base = 17
# result = 0
# power = 0

# mapping for letters
# values = {
#     'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16
# }

# for ch in reversed(num):
#     if ch.isdigit():
#         val = int(ch)
#     else:
#         val = values[ch.upper()]
    
#     result += val * (base ** power)
#     power += 1

# print(result)

# arr = [1, 2, 3, 4, 5]
# total = 0
# for num in arr:
#     total += num
# print("Total:", total)

#find maximium in an array
#assuming the array is not empty
#first element is the maximum
# compare each element with the current maximum
arr = [3, 5, 2, 8, 1]
max_value = arr[0]
for num in arr:
    if num > max_value:
        max_value = num
print("Maximum value:", max_value)

# zero to end in array
#take non zero values first
# fill remaining with zeros
arr = [4,5,0,1,9,0]
result = []
for num in arr:
    if num !=0:
        result.append(num)
zeros = len(arr) - len(result)
for i in range(zeros):
    result.append(0)    
print(result)