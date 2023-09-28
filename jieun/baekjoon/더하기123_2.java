package baekjoon;

import java.io.*;
import java.util.*;

public class 더하기123_2 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        // ArrayList를 이용하여 2차원 배열 생성
        ArrayList<String>[] arr = new ArrayList[n + 3];

        // 배열 초기화
        for (int i = 0; i <= n + 2; i++)
            arr[i] = new ArrayList<>();

        arr[1].add("1");
        arr[2].add("1+1");
        arr[2].add("2");
        arr[3].add("1+2");
        arr[3].add("1+1+1");
        arr[3].add("2+1");
        arr[3].add("3");

        for (int i = 4; i <= n + 2; i++) {
            for (int j = 1; j <= 3; j++) {
                for (String op : arr[i - j]) {
                    arr[i].add(op + "+" + j);
                }
            }
        }

        // 개수가 k보다 작을 경우 "-1" 출력
        if (arr[n].size() < k) {
            System.out.println(-1);
        } else {
            Collections.sort(arr[n]);
            System.out.println(arr[n].get(k - 1));
        }
    }
}
