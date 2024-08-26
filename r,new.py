# program to gives two Output: “abcde”, “ABCDE” for the Input String Str = “aBACbcEDed” 
str = "aBACbcEDed"
str1="".join(sorted(str))
# print(str1)
# str2=sorted.lower(str1)
lower=[]
upper=[]
for i in str1:
    if i .islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
lower_str="".join(lower)
upper_str="".join(upper)
print(lower_str, upper_str)
    
