// 실전문제: 성적이 낮은 순서로 학생 출력하기

// C++의 map은 자료를 저장할 때 내부에서 자동으로 정렬한다.
// key를 기준으로 오름차순으로 정렬한다.
// 내림차순으로 정렬하고 싶은 경우, map<int,int,greater>map1 과 같이 사용한다.

// 해당 문제에서 어려운 점은 value를 기준으로 정렬해야 한다는 것이다.
// 이 경우에는 map의 요소들을 vector로 옮겨서 정렬해야 한다.
// 1) map을 vector로 이동하기
// 2) vector를 second 기준으로 정렬하기

#include<iostream>
#include<map>

using namespace std;

static bool comp(pair<string, int> & a, pair<string,int> & b){
    return a.second < b.second;
} // 정렬 함수

int main(){
    int N;
    cin >> N;
    map<string, int> student;
    string name;
    int score;
    while (N--){ // map 입력받기
        cin >> name >> score;
        student.insert(make_pair(name,score));
        // student.insert({name,score}); 동일한 코드
    }

    vector<pair<string, int> > v(student.begin(), student.end());
    sort(v.begin(), v.end(), comp); // 벡터로 변환하여 정렬하기
    
    for (auto num : v){
        cout << num.first << " " << num.second << "\n";
    }

    return 0;
}