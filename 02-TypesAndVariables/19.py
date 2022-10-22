h = int(input("Enter your height in cm: "))
w = int(input("Enter your weight in kg: "))
bmi = w/((h/100)**2)
print("BMI index: ", round(bmi, 2))