#include <iostream>
#include <algorithm>
using namespace std;

int N, M, ans;
int map[5][501];
int dx[4] = {0, 0, -1, 1}; // 상 하 좌 우
int dy[4] = {1, -1, 0, 0}; // 상 하 좌 우
bool visited[5][501];

void DFS(int x, int y, int Sum, int Cnt){
    visited[x][y] = true; // 방문 체크

    if (Cnt == 3){ // 깊이가 4이면 종료
        ans = max(ans, Sum);
        return;
    }

    for (int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
        if (visited[nx][ny] == true) continue;

        DFS(nx, ny, Sum + map[nx][ny], Cnt + 1);
        visited[nx][ny] = false; // 방문 정보 초기화
    }
}

int main(){
    ans = 0;

    for (int i = 0; i < N; i++){ // 입력받기
        for (int j = 0; j < M; j++)
            cin >> map[i][j];
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            DFS(i, j, map[i][j], 0);
            int min = 1001;
            int tmp = map[i][j];
            for (int k = 0; k < 4; k++){
                 // 상하좌우 중 가장 작은 값 찾기
                min = min < map[i + dx[k]][j + dy[k]] ? min : map[i + dx[k]][j + dy[k]];
                tmp += map[i + dx[k]][j + dy[k]];
            }
            tmp -= min; // 가장 작은 값만 빼주기
            ans = max(tmp, ans); // DFS로 구한 최댓값과 '+' 모양 최댓값 중 더 큰 것이 정답
        }
    }

    cout << ans;
}

