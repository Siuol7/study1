x=int(input('Input a number:'))
def prime(x):
    if x==1:
        print('1 is not prime')
    elif x==2:
        print('2 is prime')
    else:
        for i in range(2,x):
            if x%i==0:
                return False 
            else:
               return True
if prime(x)==True:
     print(x,'is prime')
else: 
    print(x,'is not prime')
prime(x)