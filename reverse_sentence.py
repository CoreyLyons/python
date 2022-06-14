import string
s = str(input("Please enter a sentence. \n"))
ls = s.split(" ")
new = str()
for i in range(0,len(ls)):
    new = new + ls[len(ls)-i- 1] + ' '
for i in new:
    if i in string.punctuation:
        new = new.replace(i,"")
print(new)    
