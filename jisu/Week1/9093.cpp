using namespace std;
#include <iostream>
#include <string>
#include <stack>

int main(){
    int testCase;
    string str;
    stack <char> stack; // 선입후출을 위해 stack 사용하기

    cin >> testCase; // 테스트 케이스 입력받기
    cin.ignore();   // cin 사용 후 남은 \n 입력버퍼 지워주기
    while (testCase--){
        getline(cin,str);   // getline을 통해 한 줄씩 입력받기
        str += ' ';    // 문장 끝 바꿔주기

        for (int i = 0; i < str.size(); i++){
            if (str[i] == ' '){  // 문장 끝이거나, 띄어쓰기가 있다면
                while (!stack.empty()){ // 스택이 빌 때 까지 출력
                    cout << stack.top();
                    stack.pop();
                }   cout << ' ';    // 다 출력하고 띄어쓰기 출력
            }
            else stack.push(str[i]);
        }   cout << "\n";
    }
}