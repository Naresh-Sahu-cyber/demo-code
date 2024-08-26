# a=30
# b=50
# a,b=b,a
# print("A=",a)
# print("B",b)
sum=0
num=int(input("input number"))
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    