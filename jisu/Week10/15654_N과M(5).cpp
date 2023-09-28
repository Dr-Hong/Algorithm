#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N, M;
bool selected[9];
vector<int> arr;
vector<int> ans;

void DFS(int Cnt){
    if (Cnt == M){
        for (int i = 0; i < ans.size(); i++)
            cout << ans[i] << " ";
        cout << "\n";
        return; // return을 꼭 해줘야 Cnt = 3 일때 출력되고 종료된다
    }
    for (int i = 0; i < N; i++){
        if (selected[i] == true)
            continue; // 이미 i번째 값이 선택되었다면 넘어가기 (중복 허용X)
        selected[i] = true;
        ans.push_back(arr[i]); // i번째 값 넣기
        DFS(Cnt + 1); // 재귀 호출
        selected[i] = false;
        ans.pop_back(); // 저장된 값 비워주기
    }
}

void input(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }
}

int main(){
    input(); // 입력받기
    sort(arr.begin(), arr.end()); // 오름차순 정렬

    DFS(0);

    return 0;
}