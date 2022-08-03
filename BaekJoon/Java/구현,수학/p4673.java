package Algorithms;

public class p4673 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		int[] check = new int[10001];
		
		
		
		String num;
		for(int i = 1; i < 10001; i++) {
			num = Integer.toString(i);
			
			int sum = 0;
			for(int j = 0; j < num.length(); j++) {
				sum += (num.charAt(j) - '0');
				
			}
			sum += i;
			if (sum < 10001) {
				check[sum] = 1;
				
			}
		}

		
		for(int i = 1; i < check.length; i++) {
			if (check[i] == 0) {
				System.out.println(i);
			}
		}
		
		
		
	}

}
