def f(arr2D):
    column_sums = {}
    for row in arr2D:
        i = 0
        while i < len(row):
            if i + 1 in column_sums.keys():
                column_sums[i + 1] += row[i]
            else:
                column_sums[i + 1] = row[i]
            i += 1

    column_values = column_sums.values()
    if len(column_values) != len(set(column_values)):
        return True
    return False


if __name__ == "__main__":
    print(f([[3, 4, 2], [5, 1, 7]]))
