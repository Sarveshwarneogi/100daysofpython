bill=float(input("what is the total bill?: \n Rupees "))
peop=int(input("how many total people?:"))
tip=float(input("how much percentage tip would you like to pay? "))
per_person=(bill+0.01*tip)/peop
print(f"each person pays: {per_person} Rupees")
