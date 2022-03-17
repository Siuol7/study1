a= int(input('Input the first number:'))
b= int(input('Input the second number:'))
c= int(input('Input the third number:'))
if a<b and b<c and a<c:
    print('The median number is:',b)
elif b<a and a<c and b<c:
    print('The medium number is:',a)
else:
    print('The medium number is:',c)