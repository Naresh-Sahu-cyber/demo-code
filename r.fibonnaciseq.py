num=int(input("enter the fibonaccoi term up to which you want to print:-"))
n1=0
n2=1
print("the fibonacooi series up to",num,"term is",n1,n2, end=" ")
for i in range ( 2, num):
    n3=n1+n2
    n1=n2
    n2=n3

    print(n3, end=" ")
  