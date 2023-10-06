#include <iostream>
#include <queue>
using namespace std;

const int mxN=8, dx[4]={1, -1, 0, 0}, dy[4]={0, 0, 1, -1};
int n, m, a[mxN][mxN];
int tmp[mxN][mxN];
int ans=0;
bool vis[mxN * mxN];
vector<pair<int, int>> space;

void copy(int tmp[mxN][mxN], int a[mxN][mxN]) {
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			tmp[i][j] = a[i][j];
		}
	}
}

void bfs() {
	
	queue<pair<int, int>> q;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(tmp[i][j]==2) {
				q.push({i, j});
			}
		}
	}
	
	while(q.size()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		
		for(int k=0; k<4; k++) {
			int nx = x+dx[k];
			int ny = y+dy[k];
			
			if(nx<0 || nx>=n || ny<0 || ny>=m) continue;
			if(tmp[nx][ny]==0) {
				tmp[nx][ny] = 2;
				q.push({nx, ny});
			}
		}
	}
	
	int cnt=0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(tmp[i][j]==0) {
				cnt++;
			} 
		}
	}
	ans = max(ans, cnt);
}

void wall(int cur, int idx) {

	if(cur==3) {
		copy(tmp, a);
		int cnt=0;
		for(int i=0; i<space.size(); i++) {
			if(cnt==3) break;
			if(vis[i]) {
				int x = space[i].first;
				int y = space[i].second;
				tmp[x][y] = 1;
				cnt++;
			}
		}
		bfs();
		return;
	}
	
	for(int i=idx; i<space.size(); i++) {
		if(vis[i]) continue;
		vis[i] = true;
		wall(cur+1, i);
		vis[i] = false;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
 	cout.tie(0);
	
	cin >> n >> m;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cin >> a[i][j];
			if(a[i][j]==0) {
				space.push_back({i, j});
			}
		}
	}

	wall(0, 0);
	
	cout << ans;
}