
array=[8,1,2,6,9,12,20,3,5,2,17,6,5,231,4325,12,443,54,21,43,46,12,234,456,234,8658,214,765,32]
num=int(input('Input number needed to be found:'))
def find(z):
    array.sort()
    a=round(len(array)/2)
    if array==[]:
        print('There is no',num,' in the array')
        return
    if (array[0]==num and len(array)==1) or array[a]==num:
        print('There is ',num,' in the array')
        return
    if array[a]<num:
        del (array[0:a])
        if len(array)==1 and array[0]!=num:
            array.remove(array[0])
        find(array)
    elif array[a]>num :
        del (array[a:a*2])
        if len(array)==1 and array[0]!=num:
            array.remove(array[0])
        find(array)
    
      
find(array)