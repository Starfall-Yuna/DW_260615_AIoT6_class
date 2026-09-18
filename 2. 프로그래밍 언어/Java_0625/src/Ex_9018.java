import java.util.Scanner;

public class Ex_9018 {
	public static void main(String args[]) {
		// https://jungol.co.kr/problem/9018
		Scanner sc = new Scanner(System.in);
		
		System.out.print("두 개의 수를 입력하시오. ");
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.println(a+" + "+b+" = "+(a+b));
		System.out.println(a+" - "+b+" = "+(a-b));
		System.out.println(a+" * "+b+" = "+(a*b));
		System.out.println(a+" / "+b+" = "+(a/b));
		System.out.println(a+" % "+b+" = "+(a%b));
	}
}
