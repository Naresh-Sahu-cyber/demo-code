string=input("enter your message ")
string=string.split(" ")
for i in string:
    print(i[ ::-1], end=" ")

