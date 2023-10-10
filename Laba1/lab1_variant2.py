def find_unsorted_subarray(array, reversed = False):
    if array == sorted(array, reverse=True):
        return -1, -1

    if array == sorted(array):
        return -1, -1

    if len(array) == 0 or len(array) == 1:
        return -1, -1




    len_array = len(array) - 1

    for left_index in range(len_array):
        right_index = len_array
        while right_index > left_index:
            if array[left_index] <= array[right_index] and reversed == True:
                return left_index, right_index
            if array[left_index] >= array[right_index] and reversed == False:
                return left_index, right_index
            right_index -= 1


#print(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19, 20]))
#print(find_unsorted_subarray([0,1, 2, 3, 5,7]))
#print(find_unsorted_subarray([4,4, 3]))
print(find_unsorted_subarray([1, 2, 3, 4, 0, -1, -2], True))
print(find_unsorted_subarray([10, 9, 8, 7, 6, 0, 1, 2, -1], True))
print(find_unsorted_subarray([9, 10, 8, 6, 5], True))
print(find_unsorted_subarray([9, 8, 7, 5, 10], True))
print(find_unsorted_subarray([1, 2, 3,4], True))
print(find_unsorted_subarray([5, 4, 3, 2, 1], True))
print(find_unsorted_subarray([9,8,7,6,5], True))