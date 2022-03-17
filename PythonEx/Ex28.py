a=0
b=1
x=int(input('Input the position number of Fibonacci list:'))
for i in range (2):
    c=a+b
    b=c-a
    a=c
if c==2:
    for i in range(x-4):
        c=a+b
        b=a
        a=c
print(c)