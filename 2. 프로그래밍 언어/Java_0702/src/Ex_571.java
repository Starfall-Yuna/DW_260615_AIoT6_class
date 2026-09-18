import java.util.Scanner;

public class Ex_571 {
	// 1-1. 문자열 "~!@#$^&*()_+|" 를 출력하는 함수를 작성
	public static void printEmoji() {
		System.out.println("~!@#$^&*()_+|");
	}
	// 2-1. 문자열 "~!@#$^&*()_+|" 를 전달받은 매개변수(count) 횟수만큼 출력하는 함수를 작성
	public static void print_emoji(int count) {		// 실행할 때, int값 하나 요청
		for(int i=0;i<count;i++) {
			System.out.println("~!@#$^&*()_+|");			
		}
	}
	
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		// 1-2. 정수 하나(n)를 입력받기
		int n = scan.nextInt();
		// 1-3. n의 횟수만큼 위 함수 실행
		for(int i=0; i<n; i++) {
			printEmoji();
		}
		
		System.out.println();
		
		// 2-2. 정수 하나(num)를 입력받기
		int num = scan.nextInt();
		// 2-3. num을 매개변수 값으로 전달하면서 함수 실행 (print_emoji)
		print_emoji(num);
	}
}
