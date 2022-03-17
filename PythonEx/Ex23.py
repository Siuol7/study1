day= int(input('Input day:'))
month= int(input('Input month(in number):'))
year=int(input('Input year:'))
if year%400==0:
    year= ('leap year')
if year==('leap year') :
    if month in (1,3,5,7,8,10) and day<31:
        day+=1
    elif month==12 and day==31:
        day=1
        month=1
        year+=1
    elif month==2 and day<29:
        day+=1
    elif month in (4,6,9,11) and day <30:
        day+=1
    else:
        day=1
        month+=1

if year!=('leap year') :
    if month in (1,3,5,7,8,10) and day<31:
        day+=1
    elif month==12 and day==31:
        day=1
        month=1
        year+=1
    elif month==2 and day<28:
        day+=1
    elif month in (4,6,9,11) and day <30:
        day+=1
    else:
        day=1
        month+=1



    
print('The next day is:',day,'/',month,'/',year)