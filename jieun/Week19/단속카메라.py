# 진출지점에 대해서 오름차순으로 정렬해야, 진출지점에 카메라가 있다고 가정했을 때, 그 이후의 경로들의 진입지점이 진출지점보다 앞서면, 반드시 그 카메라에 단속된다고 장담할 수 있다.


def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
