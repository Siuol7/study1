def check(x):
    con1=0
    for i in range(1,x):
        if x%i==0:
            con1+=i
        
    if con1==x and ((con1+x)/2)==x:
        print(x,'is a perfect number')
for a in range (1,10000):
    check(a)