package baekjoon;

import java.io.*;
import java.util.Arrays;

public class 약수 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String[] mineralStr = br.readLine().split(" ");
        int[] mineral = new int[n];

        for (int i = 0; i < n; i++) {
            mineral[i] = Integer.parseInt(mineralStr[i]);
        }
        Arrays.sort(mineral);

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i; j >= 0; j--) {
                if (mineral[i] % mineral[j] == 0) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] > cnt)
                cnt = dp[i];
        }
        System.out.println(n - cnt);
    }

}
