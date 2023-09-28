package jieun.Week2;

import java.io.*;

public class 시각 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int count = 0;
        if (n >= 24)
            bw.write("잘못된 입력입니다.");
        else {
            for (int a = 0; a <= n; a++) {
                if (a % 10 == 3) {
                    count += 3600;
                    continue;
                }
                for (int b = 0; b < 60; b++) {
                    if (b % 10 == 3 || (b >= 30 && b <= 39)) {
                        count += 60;
                        continue;
                    }
                    for (int c = 0; c < 60; c++) {
                        if (c % 10 == 3 || (c >= 30 && c <= 39)) {
                            count += 1;
                        }
                    }
                }

            }
            bw.write(Integer.toString(count));
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
 * 백준 18312번 문제 ver
 * import java.io.*;
 * 
 * public class Main {
 * public static void main(String[] args) throws NumberFormatException,
 * IOException {
 * BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 * BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 * 
 * String line = br.readLine(); // 한 줄을 문자열로 입력 받음
 * String[] numbers = line.split(" ");
 * 
 * int n = Integer.parseInt(numbers[0]); // 첫 번째 정수
 * int k = Integer.parseInt(numbers[1]); // 두 번째 정수
 * 
 * int count = 0;
 * 
 * for (int a = 0; a <= n; a++) {
 * if (a % 10 == k || (a >= (k * 10) && a < ((k + 1) * 10))) {
 * count += 3600;
 * continue;
 * }
 * for (int b = 0; b < 60; b++) {
 * if (b % 10 == k || (b >= (k * 10) && b < ((k + 1) * 10))) {
 * count += 60;
 * continue;
 * }
 * for (int c = 0; c < 60; c++) {
 * if (c % 10 == k || (c >= (k * 10) && (c < (k + 1) * 10))) {
 * count += 1;
 * }
 * }
 * }
 * }
 * bw.write(Integer.toString(count));
 * bw.flush();
 * bw.close();
 * br.close();
 * }
 * }
 */