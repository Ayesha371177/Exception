try:
 age=int(input("enter age:"))
 if age<18:
  raise ValueError("age must be greater than 18 or 18")
except ValueError as e:
 print("error",e)
else:
 print("you are eligible for vote")