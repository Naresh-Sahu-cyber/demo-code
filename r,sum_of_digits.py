num=int(input("enter the number "))
temp= num
sum=0
while temp>0:
    remainder=temp%10
    sum=sum+remainder
    temp=temp//10
    # break   
    
print(sum) 

