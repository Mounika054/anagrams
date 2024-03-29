s1=input("enter a string:")
s2=input("enter another string:")
if(sorted(s1)==sorted(s2)):
    print(s1,s2,"are anagrams")
else:
    print(s1,s2,"are not anagrams")