# h=[]
# s=0
# i=0
# for i in range(0,10): #using for range loop
#   h.append(int(input("enter height:")))
#   i+=1
#   if i==10:
#     break
# k=0
# for j in h:
#   s=s+j
# a=len(h)
# print(s/a)

h=[1,4,5,7,2,5,7,8,9,7,3,8,9,.06,7698]
s=0
for i in h:
  s=s+i
  
print(s)
a=len(h)
print(s/a)
