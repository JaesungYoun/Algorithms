package Algorithms;

import java.util.Scanner;

public class p1110 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = N;
		int temp = 0;
		int cnt = 0;
		
		while(true) {
			if (N < 10) {
				temp = N;
				temp = N*10 + temp;
				
			}
			else {
				temp = (N/10) + (N%10);
				temp = (N%10)*10 + (temp % 10);
				
			}
			N = temp;	
			cnt += 1;
			if (N == M) {
				break;
			}
			
		}
	
		System.out.println(cnt);
		
		
	}

}
