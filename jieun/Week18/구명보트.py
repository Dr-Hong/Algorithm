def solution(people, limit):
    people.sort()  # 몸무게 오름차순 정렬
    answer = 0  # 필요한 구명보트 개수

    left, right = 0, len(people) - 1  # 가장 가벼운 사람과 가장 무거운 사람의 인덱스

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 함께 탈 수 있는 경우, 가장 가벼운 사람과 함께 태우고 인덱스 이동
        right -= 1  # 가장 무거운 사람은 항상 함께 타든 아니든 인덱스 이동
        answer += 1  # 구명보트 사용 개수 증가

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
