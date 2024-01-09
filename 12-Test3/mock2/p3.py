def f(d):
    count = 0
    average = sum(d.values()) / len(d.values())
    for passengers in d.values():
        if passengers > average:
            count += 1
    return count


if __name__ == "__main__":
    print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))
