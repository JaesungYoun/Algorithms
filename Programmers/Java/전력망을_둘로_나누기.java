package Programmers.Java;
import java.util.*;

public class 전력망을_둘로_나누기 {
    class Solution {
        static int cnt;

        public int solution(int n, int[][] wires) {
            int answer = Integer.MAX_VALUE;

            List<List<Integer>> mat = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                mat.add(new ArrayList<>());
            }

            for (int[] wire : wires) {
                int a = wire[0];
                int b = wire[1];
                mat.get(a).add(b);
                mat.get(b).add(a);
            }

            for (int[] wire : wires) {
                int a = wire[0];
                int b = wire[1];
                boolean[] visited = new boolean[n + 1];
                visited[b] = true;

                cnt = 1;
                dfs(a, visited, mat);
                int diff = Math.abs(cnt - (n - cnt));

                answer = Math.min(answer, diff);
            }

            return answer;
        }

        private void dfs(int start, boolean[] visited, List<List<Integer>> mat) {
            visited[start] = true;

            for (int i : mat.get(start)) {
                if (!visited[i]) {
                    visited[i] = true;
                    cnt += 1;
                    dfs(i, visited, mat);
                }
            }

        }


    }

}
