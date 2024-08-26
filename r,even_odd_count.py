# program to count Odd and Even number from given array Input: 

array=[1,2,2,5,4,6,4,1,5,2,21,122,4,5,44,52,45,56,1,54]
count=0
for i in array:
    if i%2==0:
        count+=1
print("the total even nuumbers in array is ",count)        
print("the total odd nuumbers in array is ",len(array)-count)        
