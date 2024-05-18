# Number input
print("Please enter a number?")
number = int(input())

factorise = 0

total = 1

while number > factorise:
    factorise = factorise + 1
    total = total * factorise

print(f"{total}")