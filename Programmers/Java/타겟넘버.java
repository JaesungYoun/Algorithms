package Programmers.Java;

public class 타겟넘버 {
    class Solution {
        public int solution(int[] numbers, int target) {
            return dfs(numbers, 0, 0, target);
        }

        private int dfs(int[] numbers, int depth, int result, int target) {
            int answer = 0;
            if (depth == numbers.length) {
                return result == target ? 1 : 0;
            }

            answer += dfs(numbers, depth + 1, result + numbers[depth], target);
            answer += dfs(numbers, depth + 1, result - numbers[depth], target);

            return answer;
        }

    }
}
