str = "aBACbcEDed"
lower=[]
upper=[]
for i in str:
    if i .islower():
        lower.append(i)
    
    elif i. isupper():
        upper.append(i)

lower="".join(lower)        
upper="".join(upper)   
print(("".join(sorted(lower))),("".join(sorted(upper))) )    
# print("".join(sorted(upper)))     



