def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)

def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run():
    display_chars("library.txt", 5)
    print("\n")
    print("The first line is")
    display_line("library.txt")
    print("\n")
    print("The full text is:")
    display_text("library.txt")

if __name__ == "__main__":
    run()