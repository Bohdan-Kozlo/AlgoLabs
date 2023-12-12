from math import sqrt


def find_max_height_wire(w, heights):
    max_heights = 0.0
    n = len(heights)
    i = 0
    j = 1

    while j < n:
        max_height = max(heights[i], heights[j])
        min_height = min(heights[i], heights[j])

        max_heights += sqrt(w**2 + (max_height - 1)**2)

        if min_height == heights[j]:
            heights[j] = 1

        i += 1
        j += 1

    return round(max_heights, 3)


print(find_max_height_wire(2, [4, 5, 10]))