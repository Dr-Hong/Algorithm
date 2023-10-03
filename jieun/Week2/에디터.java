package jieun.Week2;

import java.io.*;
import java.util.*;

public class 에디터 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        char[] words = br.readLine().toCharArray();
        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();

        for (char ch : words) {
            left.push(ch);
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            String[] str = br.readLine().split(" ");
            if (str[0].equals("L")) {
                if (!left.empty())
                    right.push(left.pop());
            } else if (str[0].equals("D")) {
                if (!right.empty())
                    left.push(right.pop());
            } else if (str[0].equals("B")) {
                if (!left.empty())
                    left.pop();
            } else if (str[0].equals("P")) {
                left.push(str[1].charAt(0));
            } else
                break;
        }

        while (!left.empty()) {
            right.push(left.pop());
        }

        while (!right.empty()) {
            bw.write(right.pop());
        }
        bw.flush();
        bw.close();
        br.close();
    }
}