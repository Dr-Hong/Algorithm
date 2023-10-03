package jieun.Week4;

import java.io.*;
import java.util.Arrays;

public class 접미사배열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 문자열 s 입력받기
        String s = br.readLine();

        // 문자열의 길이만큼의 크기를 가진 배열 생성
        String[] str = new String[s.length()];

        // s의 i번째 위치부터 끝까지의 접미사를 str 배열에 저장
        for (int i = 0; i < s.length(); i++) {
            str[i] = s.substring(i, s.length());
        }

        // 알파벳순 정렬
        Arrays.sort(str);

        for (int i = 0; i < s.length(); i++) {
            bw.write(str[i] + '\n');
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
