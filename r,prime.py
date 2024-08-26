a=int(input("please enter a number:-"))
if (a==0 or a==1) :
    print(a,"is not a prime number")
elif a>1:

    for i in range(2, a):
        if (a % i)==0:
            print("the number",a," is not prime")
            break

    else:
        print("the number",a,"is a prime number")    
