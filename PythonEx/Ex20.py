print("Input length of three triangle's sides")
a= int(input("Input length of the first triangle's side"))
b= int(input("Input length of the second triangle's side"))
c= int(input("Input length of the third triangle's side"))
if a==b==c:
    print('This is an equilateral triangle')
elif a==b or b==c or c==a:
    print('This is a scalene triangle')
elif a**2+b**2==c**2:
    print ('This is a right triangle') 
else:
    print('This is an isosceles triangle')