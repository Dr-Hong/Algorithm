// 핵심 개념: 브루트포스, 백트래킹

#include<iostream>
#include<vector>
using namespace std;

int N, M;
bool selected[9];
vector<int> vec;

void DFS(int Cnt){
    if (Cnt == M){
        for (int i = 0; i < vec.size(); i++)
            cout << vec[i] << " ";
        cout << "\n";
        return; // return을 꼭 해줘야 Cnt = 3 일때 출력되고 종료된다
    }
    for (int i = 1; i<= N; i++){
        if (selected[i] == true)
            continue; // 이미 i가 선택되었다면 넘어가기 (중복 허용X)
        selected[i] = true;
        vec.push_back(i);
        DFS(Cnt + 1); // 재귀 호출
        selected[i] = false;
        vec.pop_back(); // i가 2에서 시작할 때 비워줘야 한다
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    DFS(0);
    return 0;
}