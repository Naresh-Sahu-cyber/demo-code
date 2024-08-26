#  Sort an array without using in-built method 
arr = [64, 34, 25, 12, 22, 11, 90]
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        print(j)