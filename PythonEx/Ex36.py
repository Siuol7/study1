x=[-3,-2,55,-4,1/5,-2/6,7/6,-48,-9,10]
greatest_num=x[1]
sec=x[1]
for i in x:
    if greatest_num<i:
        greatest_num=i
    else:
        continue
print('So lon nhat la:',greatest_num)
for i in x:
    if sec<i and i!=greatest_num:
        sec=i
    else:
        continue
print('The second greatest number is:',sec)