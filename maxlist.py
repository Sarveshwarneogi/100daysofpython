print("enter numebers in a list:\n")
k=int(input("enter list size:"))
a=[]
for i in range(0,k):
  a.append(int(input("enter number")))
  if i==None:
    break
max=a[0]
i=0
for i in a:
  if(i>max):
    max=i
print(max)


