num=int(input("enter the number"))
temp=num
new_num=0
while temp>0:
    remainder=temp%10
    new_num=new_num*10 + remainder
    temp=temp//10
if (new_num==num):
    print("palindrom found")
else:
    print("palindrom not found")    