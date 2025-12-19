package Programmers.Java;

import java.util.*;
public class 롤케이크_자르기 {
    class Solution {
        public int solution(int[] topping) {
            int answer = 0;

            Map<Integer, Integer> toppingMap = new HashMap<>();

            for (int i = 0; i < topping.length; i++) {
                int count = toppingMap.getOrDefault(topping[i], 0);
                toppingMap.put(topping[i], count + 1);

            }

            Set<Integer> set = new HashSet<>();

            for (int i = 0; i < topping.length; i++) {
                set.add(topping[i]);
                if (toppingMap.get(topping[i]) != null) {
                    if (toppingMap.get(topping[i]) == 1) {
                        toppingMap.remove(topping[i]);
                    }
                    toppingMap.computeIfPresent(topping[i], (k, v) -> v - 1);
                }

                if (set.size() == toppingMap.size()) {
                    answer += 1;
                }

            }

            return answer;
        }
    }
}
