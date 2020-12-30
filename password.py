import random
lalpha=[]
ualpha=[]
digits=[]
spchar=[]
p=''
for i in range(65,91):
  lalpha.append(chr(i))
for i in range(97,122):
  ualpha.append(chr(i))
for i in range(49,58):
  digits.append(chr(i))
for i in range(33,48):
  spchar.append(chr(i))
a=int(input("enter length of password"))
list=lalpha+ualpha+digits+spchar
for i in range(0,a):
  ran=random.choice(list)
  p += ran
print(p)