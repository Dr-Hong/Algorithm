#include <iostream>
using namespace std;

bool map[10001][501];
int R, C, Ans = 0;
char tmp;

int dx[3] = {-1, 0, 1}; // 오른쪽 위, 오른쪽, 오른쪽 아래
int dy[3] = {1, 1, 1}; // 오른쪽 위, 오른쪽, 오른쪽 아래

// 오른쪽 위, 오른쪽, 오른쪽 아래 세 가지 경우 중
// 한 가지 경우로만 가므로 return을 통해 제어해준다.

bool DFS(int x, int y){
    map[x][y] = 1;
    if (y == C-1){
        Ans++;
        return true;
    }
    for (int i = 0; i < 3; i++){
        int next_x = x + dx[i];
        int next_y = y + dy[i];
        if (next_x >= 0 && next_y >= 0 && next_x < R && next_y < C && !map[next_x][next_y]){
            if (DFS(next_x, next_y)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);

    cin >> R >> C;

    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            cin >> tmp;
            if (tmp == '.') map[i][j] = 0;
            else if (tmp == 'x') map[i][j] = 1;
        }
    }

    for (int i = 0; i < R; i++){
        DFS(i, 0);
    }

    cout << Ans;

    return 0;
}