a = int(input("please enter a number:-"))
b=1
if (a<0):
    print("please enter a positive integer")
else:    

    for i in range (1,a+1 ):
        b=b*i
    print (b)