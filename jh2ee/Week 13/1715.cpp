#include <bits/stdc++.h>
using namespace std;

priority_queue<int, vector<int>, greater<int> > pq;
int n,m,sum;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++){
        cin>>m;
        pq.push(m);
    }

    while(pq.size()>1){
        int card1, card2;
        card1=pq.top(), pq.pop();
        card2=pq.top(), pq.pop();
        sum+=card1+card2;
        pq.push(card1+card2);
    }

    cout<<sum;

    return 0;
}