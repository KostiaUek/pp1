def find_second_largest(arr):
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


def difference(arr):
    return max(arr) - min(arr)


def median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2


def twosomethingarray(arr):
    return [min(arr), max(arr)]


def strings(arr):
    line = ""
    for e in arr:
        line += str(e)
    return "-".join(line)
