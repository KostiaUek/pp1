import csv


def f():
    with open("../data.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

        file.close()


if __name__ == "__main__":
    f()
