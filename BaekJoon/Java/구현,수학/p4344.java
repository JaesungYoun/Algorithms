package Algorithms;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p4344 {

	public static void main(String[] args) throws NumberFormatException,IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int c = Integer.parseInt(br.readLine());
		
		
				
		for (int i = 0; i < c ; i ++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int [] arr = new int[Integer.parseInt(st.nextToken())];
			int sum = 0;
			int cnt = 0;
			for (int j = 0; j < arr.length; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
				sum += arr[j];
			}
			
			double avg = sum / arr.length;
			
			for (int j = 0; j < arr.length; j++) {
				if ((double)arr[j] > avg) {
					cnt += 1;
				}
			}
			
			double rate = ((double) cnt) /arr.length * 100;
			
			bw.write(String.format("%.3f",rate) + "%" + "\n");
			bw.flush();
		}
		
		bw.close();
			
			
		}		
	}

