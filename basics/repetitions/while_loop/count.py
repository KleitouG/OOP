print("How many live cables should I avoid?")
cables_to_avoid = int(input())

cables_avoided = 0


while cables_avoided < cables_to_avoid:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} cables avoided.")