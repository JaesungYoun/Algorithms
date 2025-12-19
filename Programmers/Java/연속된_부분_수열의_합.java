package Programmers.Java;

import java.util.*;

public class 연속된_부분_수열의_합 {
    public static int[] solution(int[] sequence, int k) {
        List<int[]> answer = new ArrayList<>();

        int left = 0;
        int right = -1;
        int s = 0;

        while(true) {
            if (s < k) {
                right++;
                if (right > sequence.length - 1) {
                    break;
                }

                s += sequence[right];
            } else if (s > k) {
                s -= sequence[left];
                if (left > sequence.length -1) {
                    break;
                }
                left++;


            }

            else {
                answer.add(new int[]{left, right});
                right++;

                if (right > sequence.length -1) {
                    break;
                }
                s += sequence[right];

            }

        }
        answer.sort((a,b) -> {
            int diffA = a[1] - a[0];
            int diffB = b[1] - b[0];
            if (diffA != diffB) {
                return Integer.compare(diffA, diffB);
            }
            return Integer.compare(a[0],b[0]);
        });

        return answer.get(0);
    }
}