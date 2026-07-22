k = 2
arr = [1,2,3,4,5]
k%= len(arr)
arr = arr[k:] + arr[:k]
print(arr)