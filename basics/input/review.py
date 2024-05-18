# Display an ASCII art robot using a long string
print(""" 
##########
#  o  o  #
#  ----  #
##########

Hello, Lets play a game.
""")
# User inputs
print("Choose how many lives you would like for me to have")
lives = int(input())

print(f"Lives:  {'♥' * lives}")

print("Choose a number to multiply my lives")

lives2 = int(input())

#Total Lives

total_lives = lives * lives2


print(f"I now have {'♥' *total_lives} lives.")

#Thank you note.

print(""" 
##########
#  >  <  #
#  \__/  #
##########

THANK YOU !
""")



