a = int(input("enter a number"))
sum = 0

while a>0:
  d=int(a%10)
  sum=sum+d
  a=int(a/10)

print(sum)

