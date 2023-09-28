//이코테 5-1 스택 예제

package jieun.Week3;

import java.util.Stack;

public class 스택 {

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        stack.push(5);
        stack.push(2);
        stack.push(3);
        stack.push(7);
        stack.pop();
        stack.push(1);
        stack.push(4);
        stack.pop();

        System.out.println(stack);

        // stack 요소 역순 출력을 위한 또 다른 stack 생성
        Stack<Integer> rev_stk = new Stack<>();

        for (int i = stack.size() - 1; i >= 0; i--) {
            rev_stk.push(stack.elementAt(i));
        }

        System.out.println(rev_stk);
    }
}
