print("How far are we from the cave")
distance = int(input())

for steps in range(distance,0,-1):
    print(f"{steps} steps remaining")

print("We have reached the cave!")