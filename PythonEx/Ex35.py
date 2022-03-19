x=[-3,-2,55,-4,1/5,-2/6,-76,-48,-9,10]
greatest_num=x[1]
for i in x:
    if greatest_num<i:
        greatest_num=i
    else:
        continue
print('So lon nhat la:',greatest_num)