x= int(input('input x:'))
y= int(input('input y:'))
sum=x+y
if (x or y) %2 !=0:
    print('x and y must be even. Reinput')
    x= int(input('input x:'))
    y= int(input('input y:'))
elif sum in range(15,20):
    print('sum: 20')
else:
    print ('sum:',sum)