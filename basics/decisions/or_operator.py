print("What type of adventure should I have?")
story = input()

if story == "scary" or story == "short":
    print("Entering the dark forest!")

elif story == "safe" or story == "long":
    print("Taking the safe route!")

else:
    print("Not sure which route to take.")