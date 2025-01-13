def binary_search(array, search_value):
    if not array:  # 如果数组为空，则返回None
        return None

    left = 0
    right = len(array) - 1    

    while left <= right:
        mid = left + (right - left) // 2

        value_at_midpoint = array[mid]

        if search_value == value_at_midpoint:
            return mid
        elif search_value < value_at_midpoint:
            right = mid - 1
        elif search_value > value_at_midpoint:
            left = mid + 1

    return None


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    search_value = 7
    result = binary_search(array, search_value)
    print(result)  # 输出: 3


