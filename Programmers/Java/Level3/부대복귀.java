package Programmers.Java.Level3;
import java.util.*;


public class 부대복귀 {
    class Solution {

        static int[] distance;
        static boolean[] visited;

        public int[] solution(int n, int[][] roads, int[] sources, int destination) {
            distance = new int[n+1];
            Arrays.fill(distance, -1);

            List<List<Integer>> graph = new ArrayList<>();

            for (int i = 0; i <= n; i++) {
                graph.add(new ArrayList<>());
            }

            for (int[] road : roads) {
                int a = road[0];
                int b = road[1];
                graph.get(a).add(b);
                graph.get(b).add(a);

            }


            bfs(graph, distance, destination);

            int[] answer = new int[sources.length];
            for (int i = 0; i < sources.length; i++) {
                answer[i] = distance[sources[i]];
            }

            return answer;
        }

        private void bfs(List<List<Integer>> graph, int[] distance, int start) {
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(start);
            distance[start] = 0;

            while (!queue.isEmpty()) {
                int curr = queue.poll();

                for (int next : graph.get(curr)) {
                    if (distance[next] == -1) {
                        distance[next] = distance[curr] + 1;
                        queue.add(next);
                    }
                }
            }

        }


    }
}
