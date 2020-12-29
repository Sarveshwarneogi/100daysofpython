import random
print("choose 0 for rock, 1 for paper, and 2 for scissors")
uc=int(input("enter your choice\n"))
a=random.randint(0,2)
list=["rock","paper","scissors"]
print(f"computer chose {list[a]}")
print(f"your choice was {list[uc]}")
if(uc==a):
  print("draw")
if(uc!=a):
  if(uc==0 and a==1):
    print("computer wins")
  if(uc==1 and a==0):
    print("user wins")
  if(uc==0 and a==2):
    print("user wins")
  if(uc==2 and a==0):
    print("computer wins")
  if(uc==1 and a==2):
    print("computer wins")
  if(uc==2 and a==1):
    print("user wins")
else:
  print("wrong choice by you sir")