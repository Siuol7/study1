x= []
for i in range(100, 401):
    y = str(i)
    if (int(y[0])%2==0) and (int(y[1])%2==0) and (int(y[2])%2==0):
        x.append(y)
print( x)
