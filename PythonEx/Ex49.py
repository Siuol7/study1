x=[]
Sample_List =[1,2,3,3,3,3,4,5]
def add(*args):
    for i in Sample_List:   
        if i not in x:
            x.append(i)
    print(x)

add(Sample_List)
