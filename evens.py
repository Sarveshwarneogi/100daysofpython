x=int(input("enter starting range"))
y=int(input("enter ending range"))
s=0
for i in range(x,y+1):
  if(i%2==0):
    s=s+i
print(f"sum of evens:{s}")
