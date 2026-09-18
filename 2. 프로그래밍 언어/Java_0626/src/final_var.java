import java.util.Scanner;

public class final_var {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// 상수 :: "고정된" 값을 저장하는 공간
		//	=> Java에서는 final 키워드 사용
		
		// 상수 생성 :: final [자료형] [이름];
		// 상수 값 설정 :: [상수_이름] = [값];
		// 상수 초기화 :: final [자료형] [이름] = [값];
		final double PI = 3.14;
		// PI = 3.1415;		-> 에러, 상수는 값 변경X
		
		// 1. 반지름(r) 입력
		System.out.print("반지름을 입력해주세요. ");
		int r = scan.nextInt();
		
		// 2. r에 대한 원의 넓이 사용자에게 콘솔로 출력 (PI 활용)
		double result =  r*r*PI;
		System.out.println("원의 넓이: "+result);
	}

}



