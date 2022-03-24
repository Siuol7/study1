Sample_List =[1, 2, 3, 4, 5, 6, 7, 8, 9]
a=[]
def check(x):
    for x in Sample_List:
        if x%2==0:
            a.append(x)
    return a
print(check(Sample_List))