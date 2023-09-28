import java.io.*;

public class 사이클단어 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine()); // 단어의 개수
        String str[] = new String[n]; // 모든 단어들을 담은 str
        String str_cycle[][] = new String[n][50]; // 특정 단어의 모든 사이클 경우의 수를 담은 str
        int num = 0;
        for (int i = 0; i < n; i++) {
            str[i] = br.readLine();
            str_cycle[i][0] = str[i];
            for (int j = 1; j < str[i].length(); j++) {
                str_cycle[i][j] = str[i].substring(j) + str[i].substring(0, j);
            }
            boolean chk = true;
            for (int j = 0; chk && j < i; j++) {
                for (int k = 0; chk && k < str[j].length(); k++) {
                    if (str[i].equals(str_cycle[j][k]))
                        chk = false;
                }
            }
            if (chk)
                num++;
        }
        bw.write(Integer.toString(num));
        bw.flush();
        bw.close();
        br.close();
    }
}