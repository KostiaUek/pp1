import re


def f(first_letter, last_letter):
    count = 0
    pattern = re.compile('\bd|w.\S*')
    with open("../data.txt", "r", encoding="utf8") as file:
        words = file.read()
        # for word in words:
        #     word = word.strip()
        #     if word.startswith(first_letter) and word.endswith(last_letter):
        #         count += 1

    print(words.strip())
    matching_words = re.findall(pattern, words)

    # return count
    return len(matching_words)


if __name__ == "__main__":
    print(f("w", "d"))
