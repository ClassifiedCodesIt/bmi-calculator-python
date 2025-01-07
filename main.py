print("Welcome to the Classified BMI Calculator!")
height = float(input("What is your height in feet? (Enter as a decimal.)\n"))
heightinch = round(height * 12, 2)
print(f"Your height in inches is: {heightinch}")
weight = int(input("What is your weight in pounds?\n"))
bmi = round(weight * 703 / (heightinch * heightinch), 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")