package Programmers.Java;

import java.util.*;

public class 프로세스 {
    class Solution {
        public int solution(int[] priorities, int location) {
            int answer = 1;

            Queue<Integer> q = new ArrayDeque<>();

            for (int p : priorities) {
                q.offer(p);
            }

            while (!q.isEmpty()) {
                if (q.peek() != Collections.max(q)) {
                    if (location == 0) {
                        location = q.size() - 1;
                    } else {
                        location -= 1;
                    }
                    q.offer(q.poll());
                }

                else {
                    if (location == 0) {
                        break;
                    }
                    else {
                        location -= 1;
                    }
                    q.poll();
                    answer += 1;
                }


            }

            return answer;
        }
    }
}
