package jieun.Week2;

import java.io.*;

public class 게임개발 {
    static int direction;

    // 왼쪽으로 회전하는 함수
    public static void turn_left() {
        direction -= 1;
        if (direction == -1)
            direction = 3;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line1 = br.readLine();
        String[] numbers1 = line1.split(" ");
        int n = Integer.parseInt(numbers1[0]);
        int m = Integer.parseInt(numbers1[1]);

        String line2 = br.readLine();
        String[] numbers2 = line2.split(" ");
        int x = Integer.parseInt(numbers2[0]);
        int y = Integer.parseInt(numbers2[1]);
        direction = Integer.parseInt(numbers2[2]);

        String[] numbers = new String[n];
        int[][] map = new int[n][m];
        for (int i = 0; i < m; i++) {
            numbers[i] = br.readLine();
            String[] arr = numbers[i].split(" ");
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(arr[j]);
            }
        }

        // 북, 동, 남, 서 (0, 1, 2, 3)
        int[] dx = { -1, 0, 1, 0 };
        int[] dy = { 0, 1, 0, -1 };

        int count = 1;
        int turn_time = 0;
        int nx;
        int ny;

        while (true) {
            turn_left();
            nx = x + dx[direction];
            ny = y + dy[direction];

            // 회전 후 정면 칸을 가보지 않았다면 + 바다가 아니라면 이동
            if (map[nx][ny] == 0) {
                map[nx][ny] = 1;
                x = nx;
                y = ny;
                count += 1;
                turn_time = 0;
                continue;
            }

            // 회전 후 정면 칸을 가보았다면 + 바다라면 이동X
            else
                turn_time += 1;

            // 네 방향 모두 갈 수 없는 경우
            if (turn_time == 4) {
                nx = x - dx[direction];
                ny = y - dy[direction];
                // 뒤로 갈 수 있다면 이동
                if (map[nx][ny] == 0) {
                    x = nx;
                    y = ny;
                }
                // 뒤가 바다로 막혀있는 경우
                else
                    break;
                turn_time = 0;
            }
        }
        bw.write(Integer.toString(count));
        bw.flush();
        bw.close();
        br.close();
    }
}
