# User
print("What phrase do you require to see my Liege!")
phrase = input()

# Markings
print("\nReversing the word now your majesty...")
print("The phrase you sought out is ")

print("")

reversed = ""
# Reversed
for letter in phrase:
    reversed = letter + reversed

print(f"{reversed}")