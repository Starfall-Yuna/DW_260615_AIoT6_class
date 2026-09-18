import java.util.Scanner;

public class review {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String input = scan.next();
		
		// String(문자열) :: 
		//		[문자열 길이 제시] -> length()
		System.out.println("문자열 길이: "+input.length());
		//		[문자열 중 문자 하나 추출] -> charAt()
		System.out.println(input.charAt(1));
		System.out.println(input.charAt(3));
		//		[문자열 일부 자르기] -> substring()
		//			시작 번호 ~ 끝 번호 이전까지 슬라이싱
		System.out.println("substring(1, 3) 결과: "+input.substring(1, 3));
		//		[두 문자열이 같은지 비교] -> equals()
		//			==으로 같은지 비교가 안 되는 경우O
		//			(다르면 false, 같으면 true)
		System.out.println("equals() 결과: "+input.equals("hello"));
		System.out.println();

		// 아스키코드
		System.out.println((int)'A');	// 결과값 :: 65
		System.out.println((int)'a');	// 결과값 :: 97
		System.out.println((int)'0');	// 결과값 :: 48
	}
}
