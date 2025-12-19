package LeetCode;

public class CountSymmetricIntegers {

    public static void main(String[] args) {
        System.out.println(countSymmetricIntegers(1200,1230));
    }

    public static int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i < high + 1; i++) {
            String str_num = String.valueOf(i);
            int len = String.valueOf(i).length();
            if (len % 2 == 0) {
                int index = (int) (len / 2);
                int a = 0;
                int b = 0;
                for (int j = 0; j < index; j++) {
                    a += str_num.charAt(j) - '0';
                }
                for (int j = index; j < len; j++) {
                    b += str_num.charAt(j) - '0';
                }

                if (a == b){
                    count++;
                }
            }
        }

        return count;
    }
}
