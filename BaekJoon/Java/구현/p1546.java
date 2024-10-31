package BaekJoon.Java.구현;

import java.util.Scanner;

public class p1546 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		double[] arr = new double[N];
		
		double max = 0;
		double sum = 0;
		double new_score = 0;
		double avg;
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = sc.nextDouble();
			if(arr[i] > max) {
				max = arr[i];
			}
			
		}
		
		for(int i = 0; i < arr.length; i++) {
			new_score = arr[i]/max * 100;
			sum += new_score;
		}
		avg = sum / N;
		System.out.println(avg);
		
		
		
		sc.close();
		
		
		
		
		
		
		
	}

}
