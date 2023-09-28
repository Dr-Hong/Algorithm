//이코테 5-2 큐 예제

package jieun.Week3;

import java.util.*;

public class 큐 {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(5);
        queue.add(2);
        queue.add(3);
        queue.add(7);
        queue.remove();
        queue.add(1);
        queue.add(4);
        queue.remove();

        System.out.println(queue);

        // stack에 queue의 요소 저장
        Stack<Integer> stack = new Stack<>();

        while (!queue.isEmpty()) {
            stack.push(queue.poll());
        }

        // stack에 있는 값을 역순으로 출력

        Queue<Integer> rev_q = new LinkedList<>();

        for (int i = stack.size() - 1; i >= 0; i--) {
            rev_q.add(stack.elementAt(i));
        }

        System.out.println(rev_q);
    }
}