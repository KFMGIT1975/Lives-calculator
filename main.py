age = input("What is your current age? ")
new_age = int(age)
days = 365
weeks = 52
months = 12
h_age = 90
temp = int(h_age - new_age)*days
temp_1= int(h_age - new_age)*weeks
temp_2 = int(h_age - new_age)*months
print(f"You have {temp} days, {temp_1} weeks, and {temp_2} months left")