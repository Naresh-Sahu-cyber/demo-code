# program to gives Output: “00003241212” for the Input String Str = “32400121200” 
str = '32400121200'
count=0
for i in str:
    if i=="0" in str:
        count+=1
str=str.replace("0","")
str1="0" * count +  str 
print(str1)
