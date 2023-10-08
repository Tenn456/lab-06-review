import sys
weight = input("Enter your weight (in pounds): ")
height = input("Okay, also enter your height (in inches): ")
bmi = ((703 * float(weight)) / pow(float(height), 2))
print("Your body mass index (BMI) is " + str(bmi))