// 이코테 5-5 2가지 방식으로 구현한 팩토리얼 예제

package jieun.Week3;

public class 팩토리얼 {

    public static int factorial_iterative(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    public static int factorial_recursive(int n) {
        if (n <= 1)
            return 1;
        return n * factorial_recursive(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("반복적으로 구현 : " + factorial_iterative(5));
        System.out.println("재귀적으로 구현 : " + factorial_recursive(5));
    }
}
