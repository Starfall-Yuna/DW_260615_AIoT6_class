import java.util.Scanner;

public class Ex_518 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		// https://jungol.co.kr/problem/518
		
		// 1. 세 개의 정수를 입력
		int a = scan.nextInt();
		int b = scan.nextInt();
		int c = scan.nextInt();
		
		// 2. 합계, 평균 구하기 (평균은 int형)
		int sum = a+b+c;
		int avg = (a+b+c) / 3;
		
		System.out.println("sum : "+sum);
		System.out.println("avg : "+avg);
		
	}
}
