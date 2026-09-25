#integers
num1=1000
num2=20


#addition
total=num1+num2
print(total)


#subtraction
difference=num1-num2
print(difference)


#division
quotient=num1/num2
print(quotient)


#multiplaction
product=num1*num2
print(product)


#modulus
remainder=num1%num2
print(remainder)

y=29%5
print(y)


#floor operator
floor_division=num1//num2
print(floor_division)

x=29//5
print(x)

#exponentiation
z=20**3
print(z)


#floats
num3=999.567
num4=round(num3)
print(num4)

num5=round(num3,2)
print(num5)

#convert a float to an integer with an inbuilt function in python (56.8926 to 57)
temp=56.8926
temp=round(temp)
print(temp)

#convert the float below to give the results as follows; temp=56.8926 to 56.89
temp1=56.8926
temp1=round(temp1,2)
print(temp1)

#convert the float below to give the results; temp=56.8926 to 56.893
temp2=56.8926
temp2=round(temp2,3)
print(temp2)

#convert the float to give the results; 56.8926 to 8.926 (use string and concatenation)
temp3=56.8926
temp3=temp3%1
print(temp3)
temp3=str(temp3)
temp3=temp3[2]+"."+temp3[3:6]
print(temp3)

#convert 5678.4567 to 456.7
x=5678.4567
x=str(x)
print(x)
x1=x[5:8]
print(x1)
x2=x1+"."+x[8]
print(x2)
x2=float(x2)
print(x2)