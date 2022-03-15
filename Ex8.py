x=[]
x= input('input:').split(',')
y=[]
for i in range(len(x)):
    x[i]=int(x[i])
    if i%5==0:
        y.append(i)
print(y)
