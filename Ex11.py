for i in range (0,5,1):
    for j in range (0,5,1): 
        if (i==0 and j in (1,2,3)) or  (i in (1,2,4,5) and j in(0,4)) or (i==3 and j in(0,1,2,3,4)):
            print ('*',end="")
        else:
            print(" ",end='')
    print ()
