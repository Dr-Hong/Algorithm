//17413번 단어뒤집기2

package jieun.Week3;

import java.io.*;
import java.util.*;

public class 단어뒤집기2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        char[] ch = str.toCharArray();
        Stack<Character> stack = new Stack<>();

        int i = 0;
        while (i < ch.length) {
            if (ch[i] == '<') { // '<'를 만나면, 그대로 출력
                while (i < ch.length && ch[i] != '>') {
                    bw.write(ch[i++]);
                }
                bw.write(">");
            } else if (ch[i] != ' ') { // 문자를 만나면
                while (i < ch.length && ch[i] != ' ' && ch[i] != '<') {
                    stack.push(ch[i++]); // '<'이나 공백 전까지의 문자를 stack에 push
                }
                while (!stack.empty()) {
                    bw.write(stack.pop()); // stack의 상단의 값 삭제및 버퍼에 저장
                }
                if (i < ch.length && ch[i] == ' ') { // 공백문자라면 공백 출력
                    bw.write(" ");
                }
                if (i < ch.length && ch[i] == '<') { // '<'이라면, i값 변화없이 반복
                    continue;
                }
            }
            i++;
        }

        bw.flush();
        bw.close();
        br.close();
    }
}