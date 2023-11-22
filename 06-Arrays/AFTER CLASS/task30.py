def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 2, 9, 1, 5, 6]
array3 = [38, 27, 43, 3, 9, 82, 10]

sorted_array1 = bubblesort(array1.copy())
sorted_array2 = bubblesort(array2.copy())
sorted_array3 = bubblesort(array3.copy())

print("Original Array 1:", array1)
print("Sorted Array 1:", sorted_array1)
print("Original Array 2:", array2)
print("Sorted Array 2:", sorted_array2)
print("Original Array 3:", array3)
print("Sorted Array 3:", sorted_array3)
