package jieun.Week2;

import java.io.*;

public class 왕실의나이트 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        String[] s_str = str.split("");
        int count = 0;
        int x = s_str[1].charAt(0) - '0';
        int y = s_str[0].charAt(0) - 'a' + 1; // 1부터 시작

        // 이동 가능한 모든 범위
        int[] dx = { -2, -2, -1, -1, 1, 1, 2, 2 };
        int[] dy = { 1, -1, 2, -2, 2, -2, 1, -1 };

        for (int i = 0; i < 8; i++) {
            // 이동 후의 좌표
            int row = x + dx[i];
            int col = y + dy[i];

            // 범위 안에 존재하는 지 확인
            if (row >= 1 && row <= 8 && col >= 1 && col <= 8)
                count++;
        }

        /*
         * if문으로 모든 경우의 수 고려해보기
         * if (s_str[0].charAt(0) == 'a' || s_str[0].charAt(0) == 'h') {
         * if (s_str[1].charAt(0) == '1' || s_str[1].charAt(0) == '8')
         * count += 2;
         * else if (s_str[1].charAt(0) == '2' || s_str[1].charAt(0) == '7')
         * count += 3;
         * else
         * count += 4;
         * } else if (s_str[0].charAt(0) == 'b' || s_str[0].charAt(0) == 'g') {
         * if (s_str[1].charAt(0) == '1' || s_str[1].charAt(0) == '8')
         * count += 3;
         * else if (s_str[1].charAt(0) == '2' || s_str[1].charAt(0) == '7')
         * count += 4;
         * else
         * count += 6;
         * } else {
         * if (s_str[1].charAt(0) == '1' || s_str[1].charAt(0) == '8')
         * count += 4;
         * else if (s_str[1].charAt(0) == '2' || s_str[1].charAt(0) == '7')
         * count += 6;
         * else
         * count += 8;
         * }
         */
        bw.write(Integer.toString(count));
        bw.flush();
        bw.close();
        br.close();
    }
}
