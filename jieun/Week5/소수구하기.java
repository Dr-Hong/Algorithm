package jieun.Week5;

import java.io.*;

public class 소수구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);

        StringBuilder sb = new StringBuilder();

        boolean[] check = new boolean[end - start + 1];

        for (int i = start; i <= end; i++) {
            check[i - start] = true;
            if (i < 2) {
                continue;
            }
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    check[i - start] = false;
                    break;
                }
            }
            if (check[i - start] == true)
                sb.append(String.valueOf(i) + '\n');
        }
        System.out.print(sb);
        br.close();
    }
}
