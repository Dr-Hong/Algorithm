#include<iostream>
#define MAX 20
using namespace std;

/*

완전 탐색으로 가능한 나올 수 있는 모든 팀의 조합을 만들어보고 풀이한다.

4명이 있다고 가정해보자.
1, 2를 링크 팀으로 선택하는 경우는 2, 1을 선택하는 경우와 동일하다.
따라서 사람을 뽑을 때는 수열의 개념을 사용한다.

1, 2 를 링크 팀으로 선택했을 때, 나머지 3, 4는 스타트 팀이 된다.
3, 4 를 링크 팀으로 선택했을 때, 나머지 1, 2는 스타트 팀이 돤다.
이 경우는 능력치 차이 값이 같게 나오는 것으로, 동일한 경우이다.
따라서 1, 2 를 선택한 경우는 3, 4를 선택한 경우와 동일하므로
3, 4를 선택한 경우를 굳이 계산할 필요가 없다.
따라서 N / 2 까지 선택하면 탐색을 종료하도록 하자.

*/

int N;
int ANS = 9999999;
int arr[MAX][MAX];
bool selected[20];
bool team[20];

void DFS(int Idx){
    for (int i = 0; i < N; i++){
        if (!selected[i]){
            selected[i] = true;
            DFS(i+1);
            selected[i] = false;
        }
    }
}

void input(){ // 입력받기
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++)
            cin >> arr[i][j];
    }
}

int main(){
    input();


}