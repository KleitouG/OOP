def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for lines in file:
            print(f"Looked in {lines.strip()}")
    print("Done!")


def run():
    search("library.txt")

if __name__ == "__main__":
    run()