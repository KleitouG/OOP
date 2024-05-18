def display_ladder(steps):
    # Steps
    for step in range(steps):
        print("| |")
        print("***")

    # Bottom of ladder
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()