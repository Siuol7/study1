import random
guess= int(input('guess number:'))
a = random.randint(1,10)
print (a)
while (guess != a):
    guess= int(input('guess number:'))
    a = random.randint(1,10)
    print (a)
else:
    print('congrats')
