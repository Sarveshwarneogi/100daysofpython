c_age=int(input("what is your age\n"))
e_age=int(input("how long do you wish to live\n"))
a_left=e_age-c_age
weeks=a_left*52
months=a_left*12
days=a_left*365
print(f"You have {days} days, {months} months and  {weeks} weeks left\n")