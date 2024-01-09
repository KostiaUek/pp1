import re


def f(arr):
    count = 0
    for element in arr:
        if 4 <= len(element) <= 12 and re.search("[a-z]", element) and re.search("_", element) and re.search("[0-9]",
                                                                                                             element):
            count += 1
    return count


if __name__ == "__main__":
    print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))
