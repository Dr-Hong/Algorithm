package jieun.Week4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class 미로탈출 {

    public static int N;
    public static int M;
    public static int arr[][];

    // 오른쪽, 왼쪽, 위, 아래
    public static int[] dx = { 1, -1, 0, 0 };
    public static int[] dy = { 0, 0, 1, -1 };

    public static int bfs(int x, int y) {

        Queue<Integer> queue = new LinkedList<>();
        int count = 1;

        queue.add(x);
        queue.add(y);

        // 방문 처리
        arr[x][y] = 0;

        int now_x;
        int now_y;

        while (!queue.isEmpty()) {
            x = queue.poll();
            y = queue.poll();
            arr[x][y] = 0; // 방문처리
            for (int i = 0; i < dx.length; i++) {

                now_x = x + dx[i];
                now_y = y + dy[i];

                // 미로밖으로 나가게 된다면
                if (now_x < 0 || now_x >= N || now_y < 0 || now_y >= M) {
                    continue;
                }
                if (arr[now_x][now_y] == 1 && (now_x > x || now_y > y)) {
                    count++;
                    queue.add(now_x);
                    queue.add(now_y);
                }

            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);

        // N개의 줄에 각각 M개의 정수로 미로의 정보가 주어짐
        arr = new int[N + 1][M + 1];

        for (int i = 0; i < N; i++) {
            String[] p_arr = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(p_arr[j]);
            }
        }

        bw.write(String.valueOf(bfs(0, 0)));
        bw.close();
        br.close();
    }
}
