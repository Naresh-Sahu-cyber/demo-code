# program to gives Output: “32412120000” for the Input String Str = “32400121200”
def remove_zero(s):
    s1=s.replace("0","")
    return s1
str = '32400121200'
count=0
for i in str:
    if i=="0" in str:
        count+=1
str1=remove_zero(str)
str2=str1+ "0"*count
print(str2)


