for i in range(0,6):
    for j in range(0,6):
        if ( i in(0,5) and j in (1,2,3)) or (i in (1,2) and j ==0) or  (i==3 and j in (0,2,3,4)) or (i ==4 and j in (0,3)):
            print('*',end='')
        else:
            print(' ',end='')
    print()