from tkinter import Y


x=int(input('Input a number:'))
y={}
for i in range (x):
    y={i:i*i}
    print(y,end=',')
