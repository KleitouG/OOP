def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction")
    movement = directions()
    for index in range (len(movement)):
        print(f"{index} {movement[index]}")

def run():
    menu()


if __name__ == "__main__":
  run()

