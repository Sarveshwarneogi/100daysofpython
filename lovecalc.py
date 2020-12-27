name1=input("enter name 1")
name2=input("enter name 2")
name1= name1.lower()
name2= name2.lower()
T1=name1.count("t")
R1=name1.count("r")
U1=name1.count("u")
E1=name1.count("e")
T2=name2.count("t")
R2=name2.count("r")
U2=name2.count("u")
E2=name2.count("e")
L1=name1.count("l")
O1=name1.count("o")
V1=name1.count("v")
L2=name2.count("l")
O2=name2.count("o")
V2=name2.count("v")
L=L1+L2
O=O1+O2
V=V1+V2
E=E1+E2
T=T1+T2
R=R1+R2
U=U1+U2
true=T+R+U+E
love=L+O+V+E
per=(str(true)+str(love))
print(f"Love percentage is:"+ per)
per=int(per)
if(per>90 or per<10):
  print("coke and mentos")
elif(per>40 and per<50):
  print("You are alright")
else:
  print(f"your score is {per} percent")
