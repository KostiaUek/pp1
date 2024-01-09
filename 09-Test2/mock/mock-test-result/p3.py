def f(array2D):
    sums_rows = []
    column_element_sums = {}

    for row in array2D:
        sums_rows.append(sum(row))
        for i in range(len(row)):
            element_of_column = row[i]
            if i in column_element_sums.keys():
                column_element_sums[i] += element_of_column
            else:
                column_element_sums[i] = element_of_column

    sums_columns = list(dict(sorted(column_element_sums.items())).values())

    return sums_rows == sums_columns


if __name__ == "__main__":
    print(f([[3, 7, 2], [4, 2, 5], [5, 2, 1]]))
    print(f([[3, 7, 2], [4, 2, 5], [9, 2, 1]]))
