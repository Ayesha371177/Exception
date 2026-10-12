
try:
 print("program start")
 x=int(input("enter x value:"))
 y=int(input("enter y value:"))
 z=x/y
 print(z)
except ZeroDivisionError as e:
 print("error",e)
except ValueError as a:
 print("give only integre value",a)