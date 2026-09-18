import java.util.Scanner;

public class review_1416 {
	// 상수 :: "고정된" 값을 저장 (final)
	// 연산자 :: 
	//		- 산술연산자 :: +, -, *, /(몫), %(나머지)
	//		- 증감연산자 :: ++, --		(++num, num++)
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		
		// 1. 세 과목의 시험점수 입력 (정수)
		int s1 = scn.nextInt();
		int s2 = scn.nextInt();
		int s3 = scn.nextInt();
		
		// 2. 합격/불합격 여부 판단
		int no = 0;		// 0값을 유지하면 합격, 아니면 불합격
		if(s1<40 || s2<40 || s3<40) {		
			// 단 한과목이라도 40점 미만인 과목이 있다면 -> 불합격
			no++;
		}
		
		// double avg = (s1+s2+s3)/3;		// avg 값 :: 68.0 (몫)
		double avg = (s1+s2+s3)/(double)3;	// avg 값 :: 68.33333333 (나눗셈 결과)
		if(avg < 60) {
			// 평균이 60 미만이면 -> 불합격
			no++;
		}
		
		// 3. no값에 따른 합격/불합격 여부 출력
		switch(no) {
		case 0:
			System.out.println("합격");
			break;
		default:
			System.out.println("불합격");
		}
		
		// 삼항연산자 ? (조건문 유사)
	}

}
