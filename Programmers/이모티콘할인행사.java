package Programmers;
import java.util.*;
public class 이모티콘할인행사 {

    class Solution {
        int[] discounts = {10, 20, 30, 40};
        int maxSubscribers = 0;
        int maxSales = 0;

        public int[] solution(int[][] users, int[] emoticons) {
            List<int[]> discountCombos = generateDiscountCombinations(emoticons.length);

            for (int[] rates : discountCombos) {
                int subscribers = 0;
                int totalSales = 0;

                for (int[] user : users) {
                    int userRate = user[0];
                    int userPrice = user[1];
                    int userTotal = 0;

                    for (int i = 0; i < emoticons.length; i++) {
                        if (rates[i] >= userRate) {
                            userTotal += emoticons[i] * (100 - rates[i]) / 100;
                        }
                    }

                    if (userTotal >= userPrice) {
                        subscribers++;
                    } else {
                        totalSales += userTotal;
                    }
                }

                if (subscribers > maxSubscribers ||
                        (subscribers == maxSubscribers && totalSales > maxSales)) {
                    maxSubscribers = subscribers;
                    maxSales = totalSales;
                }
            }

            return new int[]{maxSubscribers, maxSales};
        }

        // 이모티콘 개수에 따라 가능한 할인 조합 생성 (product)
        private List<int[]> generateDiscountCombinations(int length) {
            List<int[]> result = new ArrayList<>();
            backtrack(result, new int[length], 0);
            return result;
        }

        private void backtrack(List<int[]> result, int[] current, int depth) {
            if (depth == current.length) {
                result.add(current.clone());
                return;

            }

            for (int d : discounts) {
                current[depth] = d;
                backtrack(result, current, depth+1);
            }

        }
    }

}
