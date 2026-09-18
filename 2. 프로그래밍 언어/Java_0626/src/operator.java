
public class operator {

	public static void main(String[] args) {
		// 연산자 :: 기능을 수행하는 기호
		// - 산술연산자 :: +, -, *, /(몫), %(나머지)
		System.out.println("7/5 결과(몫): "+(7/5));
		System.out.println("7%5 결과: "+(7%5));
		
		//	(int) / (int) = (int)	-> 몫 결과
		//	(double) / (int) = (double)
		//	(int) / (double) = (double)		-> 나눗셈 결과
		System.out.println("7/5.0 결과: "+(7/5.0));
		System.out.println("(double)7/5 결과: "+((double)7/5));
			// 7의 자료형(int)을 double로 "강제 타입 변환"
		
		// 7/5 나눗셈 결과를 소수점 3번째 자리까지 출력
		System.out.printf("7/5 (소수점 3번째) :: %.3f\n", (7.0/5));
		System.out.println();
		// String.format() 함수 알아보기
		
		// 대입연산자 :: = (우측의 값을 좌측의 공간에 대입한다.)
		
		// 증감연산자 :: ++(1 증가), --(1 감소)
		int count = 0;
		// count++;
		System.out.println(++count);
		// count--;
		System.out.println(--count);
	}

}
