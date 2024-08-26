num=int(input("enter the term"))
n1=0
n2=1
print(n1,end=" ")
for i in range (1,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end =" " )