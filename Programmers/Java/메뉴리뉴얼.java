package Programmers.Java;
import java.util.*;
public class 메뉴리뉴얼 {

    class Solution {

        public String[] solution(String[] orders, int[] course) {
            List<String> answerList = new ArrayList<>();

            HashMap<Character, Integer> counter = new HashMap<>();

            // 1. 각 문자의 전체 등장 횟수 카운트
            for (String order : orders) {
                for (char c : order.toCharArray()) {
                    counter.put(c, counter.getOrDefault(c, 0) + 1);
                }
            }

            // 2. 2회 이상 등장한 문자만 후보로
            List<Character> candidate = new ArrayList<>();
            for (Map.Entry<Character, Integer> entry : counter.entrySet()) {
                if (entry.getValue() >= 2) {
                    candidate.add(entry.getKey());
                }
            }

            Collections.sort(candidate);

            // 3. 각 course 길이에 대해
            for (int courseLength : course) {
                if (courseLength > candidate.size()) continue;

                List<String> combinations = new ArrayList<>();
                makeCombi(candidate, courseLength, 0, new StringBuilder(), combinations);

                HashMap<String, Integer> comboCountMap = new HashMap<>();

                for (String combo : combinations) {
                    int count = 0;
                    for (String order : orders) {
                        if (containsAll(order, combo)) {
                            count++;
                        }
                    }
                    if (count >= 2) {
                        comboCountMap.put(combo, count);
                    }
                }
                int max = 0;
                for (int val : comboCountMap.values()) {
                    if (val > max) max = val;
                }

                for (Map.Entry<String, Integer> entry : comboCountMap.entrySet()) {
                    if (entry.getValue() == max) {
                        answerList.add(entry.getKey());
                    }
                }
            }


            Collections.sort(answerList);
            return answerList.toArray(new String[0]);
        }

        // 조합 생성
        private void makeCombi(List<Character> candidate, int courseLength, int start, StringBuilder sb, List<String> result) {
            if (sb.length() == courseLength) {
                result.add(sb.toString());
                return;
            }

            for (int i = start; i < candidate.size(); i++) {
                sb.append(candidate.get(i));
                makeCombi(candidate, courseLength, i + 1, sb, result);
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        // order에 combo의 모든 문자가 포함되는지 확인
        private boolean containsAll(String order, String combo) {
            for (char c : combo.toCharArray()) {
                if (order.indexOf(c) == -1) {
                    return false;
                }
            }
            return true;
        }
    }

}
