package Programmers.Java;
import java.util.*;

public class 택배상자 {

    class Solution {
        public int solution(int[] order) {

            Deque<Integer> stack = new ArrayDeque<>();


            int i = 1;
            int now = 0;
            while (i <= order.length) {
                stack.push(i);
                while (!stack.isEmpty() && stack.peek() == order[now]) {
                    stack.pop();
                    now += 1;

                }

                i+=1;
            }



            return now;
        }
    }
}
