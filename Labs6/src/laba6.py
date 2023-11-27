def build_array(input_str):
    len_str = len(input_str)
    array = [0] * len_str
    j = 0
    i = 1

    while i < len_str:
        if input_str[i] == input_str[j]:
            array[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                array[i] = 0
                i += 1
            else:
                j = array[j - 1]

    return array


def find_indexes(any_str, search_str):
    len_search_str = len(search_str)
    len_any_str = len(any_str)
    array = build_array(search_str)
    indexes = []
    i = 0
    j = 0

    while i < len_any_str:
        if any_str[i] == search_str[j]:
            i += 1
            j += 1

            if j == len_search_str:
                indexes.append(i - j)
                indexes.append(i - 1)
                j = array[j - 1]
        else:
            if j > 0:
                j = array[j - 1]
            else:
                i += 1

    return indexes


haystack = "abracadabra"
needle = "abra"
result = find_indexes(haystack, needle)
print(result)
