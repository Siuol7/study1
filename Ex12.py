for i in range(0,6):
    for j in range (0,4):
        if (i in(0,5)and j in (0,1,2)) or (i in (1,2,3,4) and j in ( 0,3)):
            print ('*', end='')
        else:
            print (' ',end='')
    print()