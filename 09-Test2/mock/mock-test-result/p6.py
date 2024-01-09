import json


def f(years, course_name):
    count = 0
    with open("../data.json", "r", encoding="utf8") as file:
        dictionaries = json.load(file)

    for student in dictionaries:
        courses = student["studies"]["courses"]

        course_avg = 0
        for course in courses:
            if course["name"] == course_name:
                course_avg = sum(course["grades"]) / len(course["grades"])
        if student["age"] >= years and course_avg >= 4:
            count += 1
    return count


if __name__ == "__main__":
    print(f(21, "statistics"))
