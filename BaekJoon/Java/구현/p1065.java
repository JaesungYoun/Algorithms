package BaekJoon.Java.구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p1065 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String s = br.readLine();
		int N = Integer.parseInt(s);
		int hansu = 0;
		
		
		
		for (int i = 1; i <= N; i++) {
			if (i <= 99) 
				hansu += 1;
			else {
				String ss = Integer.toString(i);
				if ((ss.charAt(0) - '0')- (ss.charAt(1) -'0') == (ss.charAt(1) - '0') - (ss.charAt(2)-'0')) {
					hansu += 1;
				}
			}
		}
		System.out.println(hansu);
		
	}

}
