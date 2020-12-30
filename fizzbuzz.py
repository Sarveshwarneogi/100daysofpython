
i=1
while True:
  if i%3==0:
    if i%5==0:
      print("fizzbuzz")
    else:
      print("fizz")
  elif i%5==0:
    print("buzz")
  else:
    print(i)
  i+=1
  if(i%100==0):
    x=input("would you like to stop?\n Y/N")
    if(x=="Y"):
      break
    else:
      continue  
