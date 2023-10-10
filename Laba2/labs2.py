def min_square_board(number, width, height):

    if not (1 <= number <= 1012 and 1 <= width <= 109 and 1 <= height <= 109):
        return -1

    left = 1
    right = max(width, height)
    right *= number
    count = 0

    while left < right:
        mid = (left + right) // 2
        rows = mid // width
        cols = mid // height
        total_result = rows * cols
        count += 1
        print(count)
        if total_result >= number:
            right = mid
        else:
            left = mid + 1

    return left


result = min_square_board(16, 4, 16)

print(result)
