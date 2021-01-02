import random
word_list=["cunningham","cytoplasm","inphoenix"]
cchoice=random.choice(word_list)
c=len(cchoice)
hint=["fox attitude","human cell related","rise from the ashes"]
for i in word_list:
  if i==cchoice:
    for j in i:
      print("_", end=" ")
print('')
x=word_list.index(cchoice)
print(f"Hint is:- {hint[x]}")

def comparing():
  ch=input("enter a character")
  for i in cchoice:
    if i==ch:
      print(end="")
      print(f"{i}", end="")
    else:
      print("_")
comparing()
