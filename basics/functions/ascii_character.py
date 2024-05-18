print("Program Started!")
print("Please enter an ASCII code:")
ASCII = int(input())

if ASCII >= 32 and ASCII <= 126:
    print(f"The character represented by the ASCII value {ASCII} is: {chr(ASCII)}")
else:
    print("The character cannot be displayed.")

print("Program Ended!")