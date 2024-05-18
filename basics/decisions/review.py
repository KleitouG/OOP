print("Slay the monster!")


print("Use Sword")
damage = input()
if damage == "Sword":
    print("Flaming Sword or Lightning Sword")
    choose_sword = input()
    if choose_sword == "Flaming Sword":
        print("You burn the monster into a crisp!")

    elif choose_sword == "Lightning Sword":
        print("You electrified the monster! ")
    else:
        print("You died!")

else:
    print("You died!")