package jieun.Week2;

import java.io.*;

public class 큐 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] queue = new int[n];
        int index = 0;

        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split(" ");
            // push
            if (str[0].length() >= 4 && str[0].substring(0, 4).equals("push")) {
                queue[index++] = Integer.parseInt(str[1]);
                continue;
            }
            // pop
            else if (str[0].length() >= 3 && str[0].substring(0, 3).equals("pop")) {
                if (index == 0) {
                    bw.write("-1" + "\n");
                } else {
                    bw.write(String.valueOf(queue[0]) + "\n");
                    for (int j = 0; j < index - 1; j++) {
                        queue[j] = queue[j + 1];
                    }
                    index--;
                }
            }
            // size
            else if (str[0].length() >= 4 && str[0].substring(0, 4).equals("size"))
                bw.write(String.valueOf(index) + "\n");
            // empty
            else if (str[0].length() >= 5 && str[0].substring(0, 5).equals("empty")) {
                if (index == 0)
                    bw.write("1" + "\n");
                else
                    bw.write("0" + "\n");
            }
            // front
            else if (str[0].length() >= 5 && str[0].substring(0, 5).equals("front")) {
                if (index == 0)
                    bw.write("-1" + "\n");
                else
                    bw.write(String.valueOf(queue[0]) + "\n");
            }
            // back
            else if (str[0].length() >= 4 && str[0].substring(0, 4).equals("back")) {
                if (index == 0)
                    bw.write("-1" + "\n");
                else
                    bw.write(String.valueOf(queue[index - 1] + "\n"));
            }
            bw.flush();
        }
        bw.close();
        br.close();
    }
}
