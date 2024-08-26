# program to gives two Output: “Subburaj”, “123” for the Input String Str = “Subbu123raj”
str = "Subbu123raj"
# str="".join(sorted(str))
# print(str)
alpha=''
nume=""
for i in str:
    if i .isalpha():
        alpha=alpha+i
    elif i .isdigit():
        nume=nume+i 
print(alpha, nume)           
                