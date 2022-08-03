package Algorithms;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p3052 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int num;
		
		int[] arr = new int[10];
		
		for(int i= 0; i< 10; i++) {
			st = new StringTokenizer(br.readLine());
			num = Integer.parseInt(st.nextToken());
			arr[i] = num % 42;
			
			
		}
		int cnt = 0;
		
		for(int i = 0; i < 10; i++) {
			boolean b = false;
			for(int j = i+1; j < arr.length; j++) {
				if (arr[i] == arr[j]) {
					b = true;
					break;
				}
				
			}
			if (b == false)
				cnt++;
		}
		
		bw.write(cnt +  "\n");
		
		br.close();
		bw.flush();
		bw.close();
		
	}

}
