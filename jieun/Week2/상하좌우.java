package jieun.Week2;

import java.io.*;

public class 상하좌우 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        String[] s_str = str.split(" ");
        char[] words = new char[s_str.length];

        for (int i = 0; i < s_str.length; i++) {
            words[i] = s_str[i].charAt(0);
        }

        int x = 1;
        int y = 1;

        for (int i = 0; i < words.length; i++) {
            if (words[i] == 'L' && y > 1) {
                y -= 1; // 왼쪽으로 한 칸 이동
            } else if (words[i] == 'R' && y < n) {
                y += 1; // 오른쪽으로 한 칸 이동
            } else if (words[i] == 'U' && x > 1) {
                x -= 1; // 위로 한 칸 이동
            } else if (words[i] == 'D' && x < n) {
                x += 1; // 아래로 한 칸 이동
            }
            // 그 외의 경우는 무시
        }
        bw.write(Integer.toString(x));
        bw.write(" ");
        bw.write(Integer.toString(y));
        bw.flush();
        bw.close();
        br.close();
    }

    @Override
    public String toString() {
        return "상하좌우 []";
    }
}