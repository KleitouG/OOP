import csv


def extract(file_path):
    print("Extracting...")
    print("\n")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    print("\n")
    print(f"The extracted names are:\n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()