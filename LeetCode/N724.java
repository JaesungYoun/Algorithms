package LeetCode;

public class N724 {
    class Solution {
        public int pivotIndex(int[] nums) {
            int _sum = 0;

            for (int n : nums) {
                _sum += n;
            }

            int pivot = 0;
            int left_sum = 0;
            for (int i = 0; i < nums.length; i++) {

                pivot = i;
                _sum -= nums[i];

                if (left_sum == _sum) {
                    return pivot;
                }
                left_sum += nums[i];
            }
            return -1;
        }
    }
}
