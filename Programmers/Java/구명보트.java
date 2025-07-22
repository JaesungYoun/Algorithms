package Programmers.Java;
import java.util.*;
public class 구명보트 {
    class Solution {
        public int solution(int[] people, int limit) {
            int answer = 0;

            Arrays.sort(people);

            Deque<Integer> q = new ArrayDeque<>();
            for (int p : people) {
                q.add(p);
            }

            while (!q.isEmpty()) {
                if (q.size() == 1) {
                    answer += 1;
                    break;
                }
                if (q.peek() + q.peekLast() <= limit){
                    q.poll();
                    q.pollLast();
                } else {
                    q.pollLast();

                }
                answer += 1;
            }



            return answer;
        }
    }
}
