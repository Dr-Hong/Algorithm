package jieun.Week9;

import java.io.*;

public class 더하기123 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num_case = Integer.parseInt(br.readLine()); // 케이스 개수

        int dp[] = new int[11];
        dp[1] = 1; // 1
        dp[2] = 2; // 1+1, 2
        dp[3] = 4; // 1+1+1, 2+1, 1+2, 3

        for (int j = 4; j <= 10; j++) { // 4부터 반복
            dp[j] = dp[j - 3] + dp[j - 2] + dp[j - 1];
        }
        // dp[4] = 3의 경우+1 , 2의 경우+2, 1의 경우+3

        for (int i = 0; i < num_case; i++) {
            int num = Integer.parseInt(br.readLine());
            bw.write(String.valueOf(dp[num]) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
