
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



bmi = weight/(height**2)
bmi_rounded = round(weight/(height**2))
if bmi < 18.5:
    print(f"Your BMI is {bmi_rounded}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi_rounded}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi_rounded}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_rounded}, you obese.")
else:
    print(f"Your BMI is {bmi_rounded}, you are clinically obese.")
input("Press enter to close program.")