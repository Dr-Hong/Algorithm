import java.io.*;

public class 단어뒤집기 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            String[] words = str.split(" "); // 공백 기준으로 단어 분리
            char[] n_str = new char[20];
            int index;

            for (int j = 0; j < words.length; j++) {
                index = 0;
                for (int k = words[j].length() - 1; k >= 0; k--)
                    n_str[index++] = words[j].charAt(k);
                bw.write(String.valueOf(n_str, 0, index));
                n_str = new char[20]; // n_str 초기화
                if (j != words.length - 1) // 마지막 단어가 아니라면 공백 추가
                    bw.write(" ");
            }
            if (i < n - 1) // 마지막 문장이 아니라면 개행 추가
                bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
}