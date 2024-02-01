def check_count(citations, i):
    count = 0
    total = len(citations)  # 전체 논문 수
    for j in range(total):
        if citations[j] >= i:  # 논문이 i번 이상 인용되었다면 count +=1
            count += 1
    return count


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, max(citations) + 1):
        count = check_count(citations, i)
        if count >= i:  # i번이상 인용된 논문(count)이 i개 이상이라면
            answer = i
        else:
            break
    return answer
