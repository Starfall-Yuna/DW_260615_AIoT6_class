
public class print {
	public static void main(String[] args) {
		// 명령문 마지막에는 반드시 ;(세미콜론) 붙여야 함
		
		// 출력문 3가지 (``(백틱) 사용X)
		// System.out.println() :: 텍스트 출력한 후 줄바꿈 수행
		// System.out.print() :: 텍스트만 출력 (텍스트 지정X -> 에러)
		System.out.println("안녕하세요");		// "안녕하세요" + "\n"(줄바꿈)
		System.out.print("안녕하세요\n");		// "안녕하세요"
		
		// System.out.printf() :: 
		System.out.printf("13+7=%d", 13+7);
			// %d -> "뒤에 출력할 연산값이 있다" 암시, 13+7 결과값 출력
	}
}
