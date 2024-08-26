#  Array consists of integers and special characters,sum only integers 
a=["a","22","5","b","hh","45","2"]
a.sort()
list=[]
for i in a:
    if i .isnumeric():
        list.append(i)
        for j in range (0, len(list)):
            list[j]=int(list[j])

print(sum(list))
