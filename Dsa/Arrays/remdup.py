#Remove Duplicates from a Sorted Array
# W = Write pointer - worker
# R = Read pointer - inspect
arr = [1,2,2,2,3,4,4,5]
write = 0
for read in range(1, len(arr)):
    if arr[read] != arr[write]:
        write += 1
        arr[write] = arr[read]
print(arr[:write +1])