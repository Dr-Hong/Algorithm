#include <iostream>
#include <queue>
using namespace std;

bool connected[1001][1001]; // 인접 행렬
bool DFS_visited[1001];
bool BFS_visited[1001];
int N, M, V; // 정점의 개수, 간선의 개수, 시작할 정점

void DFS(int V){
    DFS_visited[V] = true; // 방문 체크
    cout << V << " ";
    for (int i = 1; i <= N; i++){
        if (connected[V][i] && !DFS_visited[i])
            DFS(i); // 연결된 곳 중에 아직 방문하지 않은 곳 탐색
        if (i == N)
            return;
    }
}

void BFS(int V){
    queue <int> Q;
    Q.push(V);

    while (!Q.empty()){
        int next = Q.front();
        BFS_visited[next] = true; // 방문 체크
        cout << next << " ";
        Q.pop();

        for (int i = 1; i <= N; i++){
            if (connected[next][i] && !BFS_visited[i]){
                Q.push(i);
                BFS_visited[i] = true;
            }
        }
    }
}

int main(){
    cin >> N >> M >> V;

    while (M--){ // 정점 연결
        int a, b;
        cin >> a >> b;
        connected[a][b] = true;
        connected[b][a] = true;
    }

    DFS(V);
    cout << "\n";
    BFS(V);
}