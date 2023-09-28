def maximize_score(N, M, paper):
    max_score = 0

    # 가로로 자르기
    for i in range(N):
        current_score = 0
        for j in range(M):
            current_score = current_score * 10 + paper[i][j]
        max_score = max(max_score, current_score)

    # 세로로 자르기
    for i in range(M):
        current_score = 0
        for j in range(N):
            current_score = current_score * 10 + paper[j][i]
        max_score = max(max_score, current_score)

    return max_score

# 입력 받기
N, M = map(int, input().split())
paper = []
for _ in range(N):
    row = list(map(int, input().rstrip()))
    paper.append(row)

# 최댓값 계산 및 출력
result = maximize_score(N, M, paper)
print(result)