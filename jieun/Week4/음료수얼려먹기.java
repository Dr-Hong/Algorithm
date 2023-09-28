package jieun.Week4;

import java.io.*;

public class 음료수얼려먹기 {
    public static int N;
    public static int M;
    public static int arr[][];

    public static boolean dfs(int i, int j) {

        // 범위를 벗어나는 경우
        if (i < 0 || i >= N || j < 0 || j >= M)
            return false;

        if (arr[i][j] == 0) {
            arr[i][j] = 1;
            // 상,하,좌,우 살피기
            dfs(i - 1, j);
            dfs(i, j - 1);
            dfs(i + 1, j);
            dfs(i, j + 1);
            return true;
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");

        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);

        arr = new int[N + 1][M + 1];

        for (int i = 0; i < N; i++) {
            String[] p_arr = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(p_arr[j]);
            }
        }

        int num = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (dfs(i, j)) {
                    num++;
                }
            }
        }

        bw.write(String.valueOf(num));
        bw.close();
        br.close();
    }
}
