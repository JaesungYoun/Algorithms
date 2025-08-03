package Programmers.Java.Level3;

import java.util.*;
public class 홀짝트리 {

    class Solution {

        Set<Integer> set = new HashSet<>();
        Map<Integer, List<Integer>> graph;
        int forward;
        int reverse;

        public int[] solution(int[] nodes, int[][] edges) {
            int[] answer = new int[] {0,0};

            graph = new HashMap<>();


            for (int node : nodes) {
                graph.put(node, new ArrayList<>());
            }

            for (int[] edge : edges) {
                graph.get(edge[0]).add(edge[1]);
                graph.get(edge[1]).add(edge[0]);
            }

            for (int node : nodes) {
                if (set.contains(node))
                    continue;

                forward = 0;
                reverse = 0;
                bfs(node);

                if (forward == 1) {
                    answer[0]++;
                }
                if (reverse == 1) {
                    answer[1]++;
                }

            }
            return answer;
        }

        private void bfs(int start) {
            Queue<Integer> q = new ArrayDeque<>();
            set.add(start);
            q.offer(start);

            while (!q.isEmpty()) {
                // 현재 노드
                int now = q.poll();

                // 자식의 수
                int nowCnt = graph.get(now).size();

                if (now % 2 ==0) {
                    if (nowCnt % 2 ==0) {
                        forward++;
                    } else{
                        reverse++;

                    }
                } else {
                    if (nowCnt % 2 == 1) {
                        forward++;
                    } else {
                        reverse++;
                    }
                }

                List<Integer> kids = graph.get(now);
                for (int kid : kids) {
                    if (set.contains(kid)) {
                        continue;
                    }
                    set.add(kid);
                    q.offer(kid);
                }

            }

        }
    }
}
