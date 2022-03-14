x= int(input('first number:'))
y= int(input('last number:'))
even=[]
odd=[]
for j in range(x,y):
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print('sum of odd:',len(odd))
print('sum of even :',len(even))
