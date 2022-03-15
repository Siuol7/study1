dog_age= int(input("input dog's age in human year:"))
dogage=0
for i in range(dog_age):
    if i==0:
        dogage+=10.5
    elif i==1:
        dogage+=10.5
    else:
        dogage+=4
print("Dog's age in dog's year:",round(dogage))


