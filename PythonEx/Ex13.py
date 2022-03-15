for i in range(0,6):
    for j in range(0,6):
        if (i in (0,5) and j in(0,1,2,3)) or (i in (1,4) and j==0) or (i in (2,3) and j in(0,1,2)):
            print('*',end='')
        else: 
            print(' ',end='')
    print()