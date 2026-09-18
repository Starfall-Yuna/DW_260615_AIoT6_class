
public class function {
	// 함수 :: "여러 명령문을 하나로 묶은 것"
	// 함수 생성, 함수 호출/실행 (매개변수)
	
	// * 함수 생성
//	public static [반환형, void] [함수이름](매개변수, ...){
//		실행할 명령문;
//			...
//	}
	public static void printLine() {
		for(int i=0;i<30;i++) {		// 반복문 총 30번 실행
			System.out.print("=");
		}
		System.out.println();
	}
	
	public static void main(String args[]) {
		// https://jungol.co.kr/problem/9081
		printLine();
		System.out.println("line 함수를 호출하였습니다. ");
		System.out.println("line 함수를 다시 호출합니다. ");
		printLine();
	}
}
