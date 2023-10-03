// ROT13

#include <iostream>
#include <string>
using namespace std;

int main(){
    string str;
    getline (cin,str);
    for(int i = 0; i < str.size(); i++){
        if (str[i] >= 'a' && str[i] <= 'z'){ // 소문자의 경우
            str[i] += 13;
            if (str[i] < 'a' || str[i] > 'z') str[i] -= 26;
        }
        if (str[i] >= 'A' && str[i] <= 'Z'){ // 대문자의 경우
            str[i] += 13;
            if (str[i] < 'A' || str[i] > 'Z') str[i] -= 26;
        }
        cout<<str[i];
    }
}