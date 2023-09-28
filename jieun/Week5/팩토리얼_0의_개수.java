package jieun.Week5;

import java.io.*;

public class 팩토리얼_0의_개수 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int count = 0;

        // 5로 나누며 누적합 사용
        while (num >= 5) {
            count += num / 5;
            num /= 5;
        }

        System.out.println(count);
    }
}
