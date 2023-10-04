#include <bits/stdc++.h>
 
using namespace std;
 
int R, C, cnt = 0;
int board[10001][501];
int dr[3] = {-1, 0, 1};
int dc[3] = {1, 1, 1};
 
bool DFS(int r, int c){
    if(c == C-1){
        cnt++;
        return true;
    }
    
    board[r][c] = 1;
    
    for(int i = 0; i < 3; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr >= 0 && nr < R && nc >= 0 && nc < C && !board[nr][nc]){
            if(DFS(nr, nc)) return true;
        }
    }
    
    return false;
}
 
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); cout.tie(NULL);
    
    string s;
    cin >> R >> C;
    for(int i = 0; i < R; i++){
        cin >> s;
        for(int j = 0; j < C; j++){
            if(s[j] == '.') board[i][j] = 0;
            else board[i][j] = 1;
        }
    }

    for(int i = 0; i < R; i++){
        DFS(i, 0);
    }
    cout << cnt;
    
    return 0;
}