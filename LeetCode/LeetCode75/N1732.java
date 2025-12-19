package LeetCode.LeetCode75;

public class N1732 {
    class Solution {
        public int largestAltitude(int[] gain) {

            int answer = 0;
            int [] dp = new int[gain.length + 1];
            for (int i = 1; i < dp.length; i++) {
                dp[i] = dp[i-1] + gain[i-1];
                answer = Math.max(answer, dp[i]);
            }

            return answer;
        }
    }

}
