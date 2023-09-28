//10866번 덱 문제

package jieun.Week3;

import java.io.*;

public class 덱 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] deque = new int[n];
        int index = 0;

        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split(" ");

            // push_front
            if (str[0].equals("push_front")) {
                if (index > 0) {
                    for (int j = index - 1; j >= 0; j--) {
                        deque[j + 1] = deque[j];
                    }
                }
                deque[0] = Integer.parseInt(str[1]);
                index++;
            }

            // push_back
            else if (str[0].equals("push_back")) {
                deque[index++] = Integer.parseInt(str[1]);
            }

            // pop_front
            else if (str[0].equals("pop_front")) {
                if (index > 0) {
                    bw.write(String.valueOf(deque[0]) + "\n");
                    for (int j = 0; j < index - 1; j++) {
                        deque[j] = deque[j + 1];
                    }
                    index--;
                } else
                    bw.write("-1\n");
            }

            // pop_back
            else if (str[0].equals("pop_back")) {
                if (index > 0) {
                    bw.write(String.valueOf(deque[index - 1]) + "\n");
                    index--;
                } else {
                    bw.write("-1\n");
                }
            }

            // size
            else if (str[0].equals("size")) {
                bw.write(Integer.toString(index) + "\n");
            }

            // empty
            else if (str[0].equals("empty")) {
                if (index > 0)
                    bw.write("0\n");
                else
                    bw.write("1\n");
            }

            // front
            else if (str[0].equals("front")) {
                if (index > 0)
                    bw.write(String.valueOf(deque[0]) + "\n");
                else
                    bw.write("-1\n");
            }

            // back
            else if (str[0].equals("back")) {
                if (index > 0)
                    bw.write(String.valueOf(deque[index - 1]) + "\n");
                else
                    bw.write("-1\n");
            }
            bw.flush();

        }
        bw.close();
        br.close();
    }
}