string1="listen"
string2="snlet"
string1=list(string1)
string2=list(string2)
string1=sorted(string1)
string2=sorted(string2)

if string1==string2:
    print("anagram found")
else:
    print("not found")    