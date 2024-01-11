from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    currentWeight = 0
    i = 0

    while i < len(truck_weights):
        currentWeight -= bridge.popleft()  # 매 시간마다 큐에서 하나 내보내기

        if currentWeight + truck_weights[i] <= weight:  # 다리를 건널 수 있는 경우
            bridge.append(truck_weights[i])
            currentWeight = currentWeight + truck_weights[i]
            i += 1
        else:  # 다리를 건널 수 없는 경우
            bridge.append(0)
        answer += 1

    return answer + bridge_length  # bridge_length:마지막 값이 다리를 지나는 시간
