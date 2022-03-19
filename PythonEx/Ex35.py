x=[3,2,55,4,15,26,76,48,9,10]
solonnhat=0
for i in x:
    if solonnhat-i<0:
        solonnhat=i
    else:
        continue
print('So lon nhat la:',solonnhat)