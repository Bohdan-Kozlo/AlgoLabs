def find_unsorted_subarray(array):
    if len(array) == 0 or len(array) == 1:
        return -1, -1

    len_array = len(array)
    for left_index in range(len_array):
        right_index = len_array - 1
        while right_index > left_index:
            if array[left_index] > array[right_index]:
                return left_index, right_index + 1
            right_index -= 1
    return -1, -1


print(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

print(find_unsorted_subarray([1]))
