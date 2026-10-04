#Giv#en x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.

x=7
y=14

if x%2==0:
    if y%2==0:
        print("x and y are even")
    else:
        print('only x is even')
else:
    if y%2==0:
        print('only y is even')
    else: 
        print("neither x nor y are even")

    



