print("Program Started!")

print("Please enter a standard character:")
variable = input()

if len(variable) == 1:
    print(f"The ASCII code for {variable} is {ord(variable)}")
else:
    print("A single character was expected.")

print("The program has ended!")