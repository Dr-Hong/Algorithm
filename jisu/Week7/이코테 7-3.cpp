// 이진 탐색 소스코드 구현 (반복문)

#include <bits/stdc++.h>
using namespace std;

// 참조변수로 값을 가져옴에 주의하자.
// 엠퍼센드를 빼주면 기존 벡터에 담겨있던 값을 카피하기 때문에 시간 복잡도가 O(N^2)이 된다.

int binarySearch(vector<int>& array, int target, int start, int end){
    while (start <= end){ // 반복문 구현
        int mid = (start + end) / 2;
        if (array[mid] == target) return mid;
        else if (array[mid] > target) end = mid - 1; // target이 mid보다 작은 경우
        else start = mid + 1; // target이 mid보다 큰 경우
    }
    return -1;
}

int main(){
    int n;
    cout << "생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.\n";
    cin >> n;
    vector<int> array[n];
    for (int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        array.push_back(tmp);
    }
    int result = binarySearch(array, target, 0, n-1)
    if (result == -1)
        cout << "원소가 존재하지 않습니다.\n";
    else
        cout << result + 1 << '\n'; // 현재 위치 반환, 인덱스는 0부터 시작하므로 1을 더함
    return 0;
}