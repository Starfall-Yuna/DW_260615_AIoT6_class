import java.util.Scanner;

public class Ex_531 {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		// https://jungol.co.kr/problem/531
		
		// 1. 몸무게 입력
		double weight = sc.nextDouble();
		
		// 2. 입력값에 따른 정답 출력
		if(weight <= 50.8) {
			System.out.println("Flyweight");
		}
		else if(weight <= 61.23) {
			System.out.println("Lightweight");
		}
		else if(weight <= 72.57) {
			System.out.println("Middleweight");
		}
		else if(weight <= 88.45) {
			System.out.println("Cruiserweight");
		}
		else {
			System.out.println("Heavyweight");
		}
	}
}
