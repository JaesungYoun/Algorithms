package LeetCode;

public class Maximum_Average_Subarray_I {
    class Solution {
        public double findMaxAverage(int[] nums, int k) {

            double sum = 0;
            for (int i = 0; i < k; i++) {
                sum += nums[i];
            }

            double maxSum = sum;

            for (int i = k; i < nums.length; i++) {
                sum += nums[i] - nums[i - k];
                maxSum = Math.max(sum, maxSum);
            }


            return maxSum / k;

        }
    }
}
