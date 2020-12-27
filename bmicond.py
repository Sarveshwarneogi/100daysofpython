w=float(input("weight(kg)\n"))
h=float(input("height(m)\n"))
bmi=w/(h**2)
print(f"bmi {bmi}")
if(bmi<18.5):
  print("underweight")
elif(bmi>18.5 and bmi<25):
  print("normal weight")
elif(bmi>25 and bmi<30):
  print("overweight")
elif(bmi>30):
  print("obese")
elif(bmi>35):
  print("clinically obese")

