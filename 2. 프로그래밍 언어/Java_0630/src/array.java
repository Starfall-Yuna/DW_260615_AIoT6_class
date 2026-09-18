import java.util.Scanner;

public class array {
	// 배열 :: 동일한 이름으로 여러 개의 값을 저장
	//	=> 1차원 배열
	public static void main(String args[]) {
		// 배열 초기화(값 설정 + 배열 공간 생성) ::
		//		(자료형)[] (배열이름) = {값1, 값2, ...};
		// 배열 공간 생성 ::
		//		(자료형)[] (배열이름) = new (자료형) [크기];
		// 배열 값 설정 ::
		//		(배열이름)[배열번호] = (값);
		
		// int[] s = {60, 95, 75, 44, 80};		// 값 설정 + 배열 공간 생성
		// System.out.println(s.length);		// 배열 크기 :: 5
		
		// 배열의 첫번째 공간 번호는 0번
		// int[] score = new int [5];			// 배열 공간 생성 (0번~4번, 5번X)
		// score[0] = 60;
		// score[5] = 100;		-> 에러, 배열 범위 초과
		
//		int s1 = 60;
//		int s2 = 95;
//		int s3 = 75;
//		int s4 = 44;
//		int s5 = 80;
		
//		int sum = s1+s2+s3+s4+s5;
//		System.out.println(sum/5.0);
		
		
		// 5개의 교과목 점수 입력받고, "평균 구하기"
		int[] s = new int [5];
		
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<5; i++) {
			s[i] = sc.nextInt();
		}
		
		// int sum = s[0]+s[1]+s[2]+s[3]+s[4];
		int sum = 0;
		for(int i=0;i<5;i++) {
			sum += s[i];
		}
		
		System.out.println(sum/5.0);
	}
}
