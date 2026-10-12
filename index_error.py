l1=[10,20,"abc",4.5,True]
try:
 ind=int(input("enter index:"))
 print(l1[ind])
except IndexError as i:
 print("invalid index number",i)
 