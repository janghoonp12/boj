import java.util.*;

public class Main {
    public static int function(int n, String[] arr) {
        int ans = 0;
        int[][] prefix = new int[3][n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                prefix[j][i + 1] = prefix[j][i];
            }
            if (arr[i].equals("H")) {
                prefix[0][i + 1]++;
            } else if (arr[i].equals("P")) {
                prefix[1][i + 1]++;
            } else if (arr[i].equals("S")) {
                prefix[2][i + 1]++;
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    ans = Math.max(ans, prefix[j][i] + prefix[k][n] - prefix[k][i]);
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.next();
        }
        System.out.println(function(n, arr));
        in.close();
    }
}