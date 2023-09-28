package jieun.Week7;

import java.io.IOException;
import java.util.Scanner;

public class 반복문으로구현한이진탐색 {
    public static int binary_search(int[] array, int target, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;

            if (array[mid] == target)
                return mid;
            else if (array[mid] > target)
                end = mid - 1;
            else
                start = mid + 1;
        }
        return -1;
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
