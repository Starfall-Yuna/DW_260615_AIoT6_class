import java.util.Scanner;

public class if_124 {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		
		// https://jungol.co.kr/problem/124
		int month = scn.nextInt();
		
		// switch -> if 변환 (==, ||)
		if(month == 2) {
			System.out.println(28);
		}
		else if(month==4 || month==6 || month==9 || month==11) {
			System.out.println(30);
		}
		else {
			System.out.println(31);
		}
	}
}
