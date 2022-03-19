x=[3,2,55,4,15,26,76,48,9,10]
print('In this array')
greatest_num=0
sec=0
for i in x:
    if greatest_num-i<0:
        greatest_num=i
    else:
        continue
print('The greatest number is:',greatest_num)
for i in x:
    if sec-i<0 and i!=greatest_num:
        sec=i
    else:
        continue
print('The second greatest number is:',sec)