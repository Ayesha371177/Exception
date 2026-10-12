try:
 x=int(input("enter x value"))
 y=int(input("enter y value"))
 z=x/y
except(ValueError,ZeroDivisionError) as e:
 print("error",e)
else:
 print("result:",z)