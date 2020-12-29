import random
a=[]
print("enter a list of names:\n")
c=0
k=1
while(k!=0):
  a.append(input("enter a name:"))
  c+=1
  if (a[c-1]=="1"):
    k=0
a.pop()
print(a)
size=len(a)
print(size)
b=random.randint(1,5)
print(f"{a[b]} pays the bill")