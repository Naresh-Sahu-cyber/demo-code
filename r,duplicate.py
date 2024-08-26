
# string="this is  india , and india is my country"
# myset=set(string)
# for element in myset:
#     char=0
#     for char1 in string:
#         if char1==element:
#             char +=1
#     print("the character ",element,"is ", char, "times")

string="this is  india , and india is my country"
myset=set(string)
for element in myset:
    char=0
    for char1 in string:
       if char1==element:
           char +=1
    print(element, char)       