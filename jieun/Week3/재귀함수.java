//이코테 5-3 재귀함수 예제

package jieun.Week3;

public class 재귀함수 {

    public static void recursive_function() {
        System.out.println("재귀함수를 호출합니다.");
        recursive_function();
    }

    public static void main(String[] args) {
        recursive_function();
    }
}