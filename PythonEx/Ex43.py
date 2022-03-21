a=int(input('Input a number:'))
b=int(input('Input a number:'))
c=int(input('Input a number:'))
def max1(a,b):
    if a>b:
        return a
    else:
        return b
max2= max1(c,max1(a,b))
print(max2)