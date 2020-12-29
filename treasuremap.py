print("x marks the treasure")
l1=[]
l2=[]
l3=[]
i=0
while True:
  if i<3:
    l1.append(input("enter characters in 1st list"))
  if i>2 and i<6:
    l2.append(input("enter characters in 2nd list"))
  if i>5 and i<9:
    l3.append(input("enter characters in 3rd list"))
  if i==9:
    break
  i+=1
print("where would you like to plant the treasure?\n marked with X")
x=int(input("enter the row"))
y=int(input("enter the column"))
if (x==1):
  l1[y-1]="x"
if (x==2):
  l2[y-1]="x"
if (x==3):
  l3[y-1]="x"


print(f"{l1} + \n")
print(f"{l2} + \n")
print(f"{l3} + \n")

     

