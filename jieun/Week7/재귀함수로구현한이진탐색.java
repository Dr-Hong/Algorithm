package jieun.Week7;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 재귀함수로구현한이진탐색 {
    public static int binary_search(int[] array, int target, int start, int end) {
        if (start > end)
            return -1;
        int mid = (start + end) / 2;
        if (array[mid] == target)
            return mid;
        else if (array[mid] > target)
            return (binary_search(array, target, start, mid));
        else
            return (binary_search(array, target, mid + 1, end));
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        // 원소의 개수(n)와 찾고자 하는 값(target)을 입력받기
        int n = sc.nextInt();
        int target = sc.nextInt();

        // 전체 원소 입력받기
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        int result = binary_search(array, target, 0, n - 1);

        if (result == -1)
            System.out.println("원소가 존재하지 않습니다.");
        else
            System.out.println(result + 1);
    }
}