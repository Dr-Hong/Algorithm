package jieun.Week7;

import java.io.*;
import java.util.StringTokenizer;

public class 순차탐색 {
    public static int sequential_search(int n, String target, String[] array) {
        for (int i = 0; i < n; i++) {
            if (array[i].equals(target))
                return (i + 1);
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.");
        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st1.nextToken());
        String target = st1.nextToken();

        System.out.println("앞서 적은 원소 개수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.");
        StringTokenizer str2 = new StringTokenizer(br.readLine(), " ");
        String[] array = new String[n];
        for (int i = 0; i < n; i++) {
            array[i] = str2.nextToken();
        }

        System.out.println(sequential_search(n, target, array));
    }
}