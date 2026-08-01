# 2 loops are there in pattern
#outerloop  - rows
#innerloop - columns - print()
#0 1 2 3 4
# for i in range(6): 
#     for j in range(i+1): # 1 2 3 4 5
#         print("*",end=" ")
#     print()
    
# n = int(input("Enter a number:"))
# for i in range(n):
#     for j in range(n+1):
#         print("*",end="")
#     print()
# n = int(input("Enter a number: "))

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#           print("*",end=" ")
#     print()
    
    
#square pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
    
#left trraingle
# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#Inverted Triangle Pattern.
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#right aligned traingle
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
n = 5

for i in range(1, n + 1):
    print("  " * (n - i),end =" ")
    print("* "*i)
    
#number triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
    
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()