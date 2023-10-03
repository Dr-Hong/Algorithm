# 분할정복

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    # tail에서 pivot보다 작거나 같은 요소들로 이루어진 새로운 리스트를 생성
    left_side = [x for x in tail if x <= pivot]

    # tail에서 pivot보다 큰 요소들로 이루어진 새로운 리스트를 생성
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
