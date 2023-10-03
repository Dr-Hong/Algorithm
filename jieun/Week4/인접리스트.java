//이코테 5-7 인접리스트 예제

package jieun.Week4;

import java.util.ArrayList;

public class 인접리스트 {

    // 정점(노드)의 인덱스와 해당 정점까지의 거리 등을 저장하는 클래스
    static class Node {

        private int index;
        private int distance;

        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        public void show() {
            System.out.print("[" + this.index + "," + this.distance + "] ");
        }
    }

    public static void main(String[] args) {

        // null로 초기화
        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();

        // 빈 ArrayList로 초기화
        for (int i = 0; i < 3; i++) {
            graph.add(new ArrayList<Node>());
        }

        graph.get(0).add(new Node(1, 7));
        graph.get(0).add(new Node(2, 5));

        graph.get(1).add(new Node(0, 7));

        graph.get(2).add(new Node(0, 5));

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < graph.get(i).size(); j++) {
                graph.get(i).get(j).show();
            }
            System.out.println();
        }
    }

}
