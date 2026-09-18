import java.util.Scanner;

public class condition2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// 조건문(2) :: switch
		//	=> switch, case, break, default
		
		// https://jungol.co.kr/problem/124
		// 1. 평년의 월로 1 ~ 12사이의 정수를 입력
		int month = scan.nextInt();
		
		// 2. 월의 총 일수를 출력
		switch(month) {
		case 1:
		case 3:		// month == 1 || month == 3
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			System.out.println(31);
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			System.out.println(30);
			break;
		case 2:
			System.out.println(28);
			break;
		}
	}

}
