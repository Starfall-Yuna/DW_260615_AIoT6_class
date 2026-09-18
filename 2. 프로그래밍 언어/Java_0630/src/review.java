
public class review {
	// 반복문 :: 특정 명령문을 "일정 횟수만큼(조건식) 반복"하여 수행
	//		=> "언젠가는 종료해야함"
	//		=> while문, for문 (do-while문)
	
//	for(제어변수 선언; 조건문; 제어변수 연산) {
//		반복할 명령문
//	}
	public static void main(String args[]) {
		// "1부터 20까지의 홀수만 순차 출력"
		
		// while문 (1)
		int i=1;
		while(i<=20) {
			if(i%2 != 0) {
				System.out.print(i+" ");	// i 출력값 뒤로 공백을 연결
			}
			// i++ 조건문 안에 넣으면 :: i값이 2를 유지
			
			i++;
		}
		System.out.println();
		// while문 (2)
		int num=1;
		while(num<=20) {
			System.out.print(num+" ");
			
			num+=2;		// 루프 한번 돌때, num에 2 추가
		}
		System.out.println();
		
		// while(2) -> for문 변형
		for(int n=1; n<=20; n+=2) {
			System.out.print(n+" ");
		}
	}
}





