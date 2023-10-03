import java.io.*;
import java.util.Arrays;

public class 동일한단어그룹화하기 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine()); // 단어의 개수
        String str[] = new String[n]; // 정렬 전 단어들을 담은 str
        String sorted_str[] = new String[n]; // 정렬 후 단어들을 담은 str
        for (int i = 0; i < n; i++) {
            str[i] = br.readLine(); // 단어 입력
            char str_temp[] = str[i].toCharArray(); // 단어를 char형으로 변환하여 str_temp[]에 저장
            Arrays.sort(str_temp); // char형으로 변환한 단어들을 sort
            String sorted_word = new String(str_temp); // char형으로 변환한 sort된 단어들을 String으로 변환
            sorted_str[i] = sorted_word; // sort된 String을 sorted_str[]에 저장
        }

        Arrays.sort(sorted_str);
        int num = n; // 초기 그룹의 개수는 n개
        for (int i = 1; i < n; i++) {
            if ((sorted_str[i - 1].equals(sorted_str[i]))) {
                num--;
            }
        }

        bw.write(Integer.toString(num));
        bw.flush();
        bw.close();
        br.close();
    }
}
