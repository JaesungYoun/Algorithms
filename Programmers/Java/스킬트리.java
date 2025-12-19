package Programmers.Java;

import java.util.*;

public class 스킬트리 {
    class Solution {
        public int solution(String skill, String[] skill_trees) {
            int answer = 0;

            Set<Character> set = new HashSet<>();

            for (int i = 0; i < skill.length(); i++){
                set.add(skill.charAt(i));
            }

            for (String sk : skill_trees) {
                int idx = 0;
                boolean available = true;
                for (int i = 0; i < sk.length(); i++) {

                    if (set.contains(sk.charAt(i))) {
                        if (skill.charAt(idx) != sk.charAt(i)) {
                            available = false;
                            break;
                        }
                        idx += 1;
                    }
                }

                if (available)
                    answer += 1;
            }

            return answer;
        }
    }
}
