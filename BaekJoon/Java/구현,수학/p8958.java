package Algorithms;

import java.util.Scanner;

public class p8958 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		String[] arr = new String[N];
		
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = sc.next();
			int score = 0;
			int result = 0;
			for(int j = 0; j < arr[i].length();j++) {
				if (arr[i].charAt(j) == 'X') {
					score = 0;
				}
				else {
					score += 1;
				}
				result += score;
				
			}
			System.out.println(result);
			
		}
		
		sc.close();
		
		
		
		
	}

}
