print("Towards which direction should I paint (up, down, left or right)?")
direction = input()
# ELSE IF

if direction == "up":
    print("I am painting in the upward direction!")

elif direction == "down":
    print("I am painting in the downward direction!")

elif direction == "left":
    print("I am painting in the left direction!")

elif direction == "right":
    print("I am painting in the right direction!")

else:
    print("That is not a direction!")