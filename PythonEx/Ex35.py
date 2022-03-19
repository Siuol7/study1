x = [1,111,2,2,2,2,3,3,3,3,4,4,4,4]
if x==[]:
    print('Lack of data')
else:
    greatest_num=x[0]
    sec=x[0]
    for i in x:
        if greatest_num<i:
            greatest_num=i
        else:
            continue
    print('The greatest number is:',greatest_num)