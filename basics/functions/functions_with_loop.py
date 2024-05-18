def cross_bridge(steps):

    for step in range(steps):
        print("Crossed step.")

    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

# calls to function
cross_bridge(4)
cross_bridge(8)