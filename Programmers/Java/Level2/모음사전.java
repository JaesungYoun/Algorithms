package Programmers.Java.Level2;

import java.util.*;

public class 모음사전 {

    class Solution {
        static List<String> result = new ArrayList<>();
        static char[] alpha = {'A', 'E', 'I', 'O', 'U'};

        public int solution(String word) {
            dfs("");
            return result.indexOf(word);
        }

        public void dfs(String current) {
            result.add(current);

            if (current.length() == 5) {
                return;
            }

            for (int i = 0; i < alpha.length; i++) {
                dfs(current + alpha[i]); // 문자열은 immutable, 새로 만들어짐
            }
        }
    }

}
