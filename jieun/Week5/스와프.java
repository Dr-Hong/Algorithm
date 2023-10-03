package jieun.Week5;

import java.io.*;

public class 스와프 {
    static void swap(int[] arr) {
        int temp = arr[0];
        arr[0] = arr[1];
        arr[1] = temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = { 3, 5 };
        swap(arr);

        int i = 0;
        while (i < arr.length) {
            bw.write(String.valueOf(arr[i]) + " ");
            i++;
        }
        bw.flush();
        bw.close();
    }

}
