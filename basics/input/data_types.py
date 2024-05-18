print("What is your name human")
name = input()

print("How old are you?")
age = int(input())

print("How tall are you? (Meters)")
height = float(input())

print("How much do you weight (Kg)")
weight = float(input())
#BMI
bmi = weight / (height ** 2)

#Display Answers for bot

print(f"{name} you are {age} years old and your bmi is {bmi}")