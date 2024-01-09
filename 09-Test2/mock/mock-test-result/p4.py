def f(subjects):
    for key in subjects.keys():
        value = subjects[key]
        value_average = sum(value) / len(value)
        subjects[key] = value_average

    max_value = max(subjects.values())

    for key in subjects.keys():
        value = subjects[key]
        if value == max_value:
            return key
    return None


if __name__ == "__main__":
    print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))
