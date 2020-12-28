a=[""]
print("enter a list of names:\n")
c=0
for i in a:
  a=a.append(input("enter a name:"))
  c+=1
  if a[c]=="1":
    break
print(a)