from functools import cmp_to_key


def cmp(a, b):
    sa = str(a)
    sb = str(b)
    if sa + sb > sb + sa:
        return 1
    else:
        return -1


def solution(numbers):
    numbers.sort(key=cmp_to_key(cmp), reverse=True)  # cmp함수로 비교후 내림차순으로 정렬
    numbers = list(map(str, numbers))
    answer = "".join(numbers)
    if answer[0] == "0":  # 답이 0 일경우 0 반환
        return "0"
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
