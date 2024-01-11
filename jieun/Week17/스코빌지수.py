import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    max_count = len(scoville) / 2
    i = 0
    while i < k:
        new_scov = heapq.heappop(scoville)  # 가장 작은 값 삭제
        new_scov += heapq.heappop(scoville) * 2  # 두 번째로 작은 값 2배하여 저장
        heapq.heappush(scoville, new_scov)
        i += 1
        if i > max_count:
            print(i)
            print(max_count)
            return -1

    return i


def main():
    scoville = [5, 3, 9, 10, 12]
    k = 2
    solution(scoville, k)


main()
