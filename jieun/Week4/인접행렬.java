//이코테 5-6 인접행렬 예제

package jieun.Week4;

public class 인접행렬 {
    public static void main(String[] args) {

        int INF = 99999999;
        int graph[][];
        graph = new int[][] {
                { 0, 7, 5 },
                { 7, 0, INF },
                { 5, INF, 0 }
        };

        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                System.out.print(graph[i][j] + " ");
            }
        }
    }
}
