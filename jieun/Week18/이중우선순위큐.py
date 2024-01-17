import heapq


def solution(operations):
    maxq = []
    minq = []

    while operations:
        s_sol = operations.pop(0).split(" ")

        if s_sol[0] == "I":
            num = int(s_sol[1])
            heapq.heappush(maxq, -num)  # 최대힙에 삽입
            heapq.heappush(minq, num)  # 최소힙에 삽입
        else:
            if s_sol[1] == "1" and maxq:
                max_val = heapq.heappop(maxq)
                minq.remove(-max_val)  # 최대값 remove
            elif s_sol[1] == "-1" and minq:
                min_val = heapq.heappop(minq)
                maxq.remove(-min_val)  # 최소값 remove

    if minq and maxq:  # 큐가 비어있지 않으면 최대, 최소값 반환
        return [-maxq[0], minq[0]]
    else:  # 큐가 비어있으면 [0, 0] 반환
        return [0, 0]


result = solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(result)
