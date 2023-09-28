// 팩토리얼
#include <iostream>
using namespace std;
int factorial(int n){
    if(n > 2)
    n *= factorial(n-1);
    return n;
}
int main(void){
    int num, result = 1; // fac(0)은 1이므로 1로 세팅
    cin>>num;
    if(num!=0)
        result = factorial(num);
    cout<<result;
}
