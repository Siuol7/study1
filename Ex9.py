x= input('input:')
a=b=0
for i in x:
    if i.isdigit():
        a=a+1
    elif i.isalpha():
        b=b+1
    else:
        continue
print ('Digit:',a,'Alpha:',b)