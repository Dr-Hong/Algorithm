import java.io.*;

public class 스택 {
    static class Stack {
        int ptr; // 스택 포인터
        int[] stk;

        public Stack(int capacity) {
            ptr = 0;
            stk = new int[capacity];
        }

        public void push(int x) {
            stk[ptr++] = x;
        }

        public int pop() {
            if (ptr == 0)
                return -1;
            return (stk[--ptr]);
        }

        public int size() {
            return ptr;
        }

        public int empty() {
            if (ptr == 0)
                return 1;
            return 0;
        }

        public int top() {
            if (ptr == 0)
                return -1;
            return (stk[ptr - 1]);
        }

    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 명령어 수 입력
        int n = Integer.parseInt(br.readLine());

        // 명령어 수 크기의 Stack 객체 생성
        Stack stack = new Stack(n);

        for (int i = 0; i < n; i++) {
            String str = br.readLine();

            if (str.contains("push")) {
                String spt[] = str.split(" ");
                stack.push(Integer.parseInt(spt[1]));
            }

            else if (str.equals("pop")) {
                bw.write(Integer.toString(stack.pop()) + "\n");
            }

            else if (str.equals("size")) {
                bw.write(Integer.toString(stack.size()) + "\n");
            }

            else if (str.equals("empty")) {
                bw.write(Integer.toString(stack.empty()) + "\n");
            }

            else if (str.equals("top")) {
                bw.write(Integer.toString(stack.top()) + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

}
