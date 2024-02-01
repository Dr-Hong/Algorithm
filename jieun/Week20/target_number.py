def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(i, result):  # i는 numbers의 인덱스
        if i == n:
            if result == target:
                nonlocal answer  # 중첩 함수에서 외부 함수의 변수를 사용하고자 할 때 사용
                answer += 1
            return
        else:
            dfs(i + 1, result + numbers[i])
            dfs(i + 1, result - numbers[i])

    dfs(0, 0)
    return answer
