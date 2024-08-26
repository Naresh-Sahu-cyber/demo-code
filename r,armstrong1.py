num=int(input("Please enter the number"))
temp=num
sum=0
# if ((len(str(num)))==3):
while temp>0:
    new_num=temp%10
    sum=sum+ new_num**((len(str(num))))
    temp=temp//10

if (num==sum):
    print("the number is amstrong1 number")
else :
    print("the number is not an amstrong1r number")    

# elif(len(str(num)))==4:
#     while temp>0:
#         new_num=temp%10
#         sum+=new_num**4
#         temp//=10
#     if (num==sum):
#         print("the number is amstrong2 number")
#     else :
#         print("the number is not an amstrong2 number")    
# else:        
#     print("enter a 3 or 4 digit number")

        