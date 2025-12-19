package Programmers.Java.Level3;
import java.util.*;


public class 봉인된주문 {
    class Solution {
        public String solution(long n, String[] bans) {

            Arrays.sort(bans, (o1, o2) -> {
                if (o1.length() != o2.length()) {
                    return Integer.compare(o1.length(), o2.length());
                } else {
                    return o1.compareTo(o2);
                }
            });

            int banCount = 0;

            for (int i = 0; i < bans.length; i++) {
                long ban_num = 0;
                char[] c_arr = bans[i].toCharArray();

                for (int j = 0; j < c_arr.length; j++) {
                    ban_num += ((long) (Math.pow(26, c_arr.length - 1 - j)) * (c_arr[j] - 'a' +1));

                }

                if (ban_num - banCount <= n) {
                    banCount++;
                }
            }

            n += banCount;

            String answer = "";

            while (n > 0) {
                long rem = (n % 26);
                n = n / 26;

                if (rem == 0) {
                    answer = 'z' + answer;
                    n = n - 1;
                } else {
                    answer = (char) ('a' + rem - 1) + answer;

                }

            }

            return answer;
        }
    }
}
