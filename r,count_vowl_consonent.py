string="hi , hello"
# string=list(string)
# print(string)
string=string.replace(" ","")
string=string.replace(",","")
count=0
for i in string:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
    # print(count)    

if count==0:
    print("no vowl")

else:
    print("the number of vowls is",count) 
    print("the number of consonent are",len(string)-count)       