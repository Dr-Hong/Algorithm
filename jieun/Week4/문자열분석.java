package jieun.Week4;

import java.io.*;

public class 문자열분석 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = "";
        int low_count;
        int up_count;
        int num_count;
        int space_count;

        while ((str = br.readLine()) != null && !str.isEmpty()) {
            // 변수 초기화
            low_count = up_count = num_count = space_count = 0;
            for (int j = 0; j < str.length(); j++) {
                Character ch = str.charAt(j);
                if (Character.isLowerCase(ch) == true) {
                    low_count++;
                } else if (Character.isUpperCase(ch) == true) {
                    up_count++;
                } else if (Character.isDigit(ch) == true) {
                    num_count++;
                } else if (ch == ' ') {
                    space_count++;
                }
            }
            bw.write(low_count + " " + up_count + " " + num_count + " " + space_count + '\n');
        }
        bw.flush();
        bw.close();
        br.close();
    }
}