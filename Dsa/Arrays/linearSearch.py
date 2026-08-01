arr = [12,35,9,40,18,99]

target = 99

found = False

for num in arr:
    if num == target:
        found = True
        break
print(found)
#time complexity 0(1)
#worst Case: 0(n)