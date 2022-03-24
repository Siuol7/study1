
w= input('Input your string:')
def check(*args):
    countu=0
    countl=0
    for i in w:
        if i.isupper():
            countu+=1
        if i.islower():
            countl+=1
    print('Lowercase words:',countl)
    print('Uppercase words:',countu)
check(w)