package Programmers.Java;

import java.util.*;

public class 귤_고르기 {
    public class Solution {
        public int solution(int k, int[] tangerine) {
            Map<Integer, Integer> countMap = new HashMap<>();

            // 각 크기의 귤 개수 세기
            for (int t : tangerine) {
                countMap.put(t, countMap.getOrDefault(t, 0) + 1);
            }

            // 개수 기준으로 내림차순 정렬

            List<Map.Entry<Integer, Integer>> countList = new ArrayList<>(countMap.entrySet());
            countList.sort((a,b) -> Integer.compare(b.getValue(), a.getValue()));

            int sum = 0; // 귤 판매 개수
            int answer = 0; // 종류 수

            System.out.println(countList);
            for (Map.Entry<Integer, Integer> entry : countList) {
                if (sum >= k) break;

                sum += entry.getValue();
                answer++;
            }

            return answer;
        }
    }


}


