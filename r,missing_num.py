# Find the missing number in an Array 
array=[1,2,3,5,6]
n=len(array)+1
total=(n*(n+1))//2
sum_array=sum(array)
print("the missing number is",total-sum_array)