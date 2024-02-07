#include<vector>
#include <queue>
using namespace std;
 
int visited[101][101];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
 
int solution(vector<vector<int> > maps)
{
    int answer = 0;
    queue<pair<int,pair<int,int> > > q;
    q.push(make_pair(1,make_pair(0,0)));        // 시작 위치 넣기
    visited[0][0] = true;
    while (!q.empty())
    {
        int x = q.front().second.first;
        int y = q.front().second.second;
        int time = q.front().first;
        if (x == maps[0].size()-1 && y == maps.size() -1)   // 도착 지점 체크
        {
            answer = time;
            break;
        }
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int xx = x + dx[i];
            int yy = y + dy[i];
            if (xx >= 0 && yy >= 0 && xx < maps[0].size() && yy< maps.size())       // 범위 지정
            {
                if (!visited[yy][xx] && maps[yy][xx] == 1)      // 방문했던 곳 and maps 상 길인 지점                                                     
                {
                    visited[yy][xx] = true;
                    q.push(make_pair(time +1, make_pair(xx,yy)));
                }
            }
        }
    }
    if (answer == 0)        // answer = 0 이면 위 bfs에서 도착지점을 못찾은것
        answer = -1;
    return answer;
}