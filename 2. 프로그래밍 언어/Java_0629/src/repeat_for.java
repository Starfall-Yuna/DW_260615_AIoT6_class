import java.util.Scanner;

public class repeat_for {
	// 반복문 :: while, for (+ do-while)
	public static void main(String[] args) {
		// for문
//		for(제어변수 선언식 ;조건식* ; 제어변수 연산식) {
//			반복할 명령문;
//		}
		
		Scanner scn = new Scanner(System.in);
		
		// 2개의 정수 입력(n<m)받은 뒤
		int n = scn.nextInt();
		int m = scn.nextInt();
		
		// n부터 m까지 정수를 출력하는 프로그램 작성
		for(int i=n; i<=m; i++) {		// 1부터 15까지 -> n부터 m까지
			System.out.print(i+" ");
		}
	}

}
