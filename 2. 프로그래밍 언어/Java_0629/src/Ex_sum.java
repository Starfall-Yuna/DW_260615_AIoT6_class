import java.util.Scanner;

public class Ex_sum {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		
//		아래의 연산이 총 3번 이루어지게끔 구성하라
		for(int i=1; i<=3; i++) {	// i :: 1, 2, 3
//			1) 2개의 실수 입력 받기
			double a = scn.nextDouble();
			double b = scn.nextDouble();
			
//			2) 몇번째 연산인지를 출력하기
			System.out.println(i+"번째 연산");
			
//			3) 두 실수의 합을 출력하기
			System.out.println(a+b);
		}
	}

}
