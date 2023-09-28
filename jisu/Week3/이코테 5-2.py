from collections import deque
#파이썬에서 큐 구현하기 위해 쓰는 라이브러리 import

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() #queue에 reverse 함수 -> 역순 출력
print(queue)