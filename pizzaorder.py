size=input("what pizza do you want?\n Small(S);Medium(M);Large(L)")
pepperoni=input("do you need pepperoni?\n Yes(Y);No(N)")
cheese=input("do you need extra cheese?\n Yes(Y);No(N)")
if(size=="S"):
  if(pepperoni=="Y"):
    price=15+2
  elif (pepperoni=="N"):
    price=15
if(size=="M"):
  if(pepperoni=="Y"):
    price=20+3
  elif (pepperoni=="N"):
    price=20
if(size=="L"):
  if(pepperoni=="Y"):
    price=25+3
  elif (pepperoni=="N"):
    price=25
if(cheese=="Y"):
  price=price+1
else:
  pass
print(price)
  
