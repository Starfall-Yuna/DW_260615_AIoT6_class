import java.util.Scanner;

public class Ex_597 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 두 개의 문자열을 입력받아서
		String s1 = sc.next();
		String s2 = sc.next();
		
		// 두 문자열의 길이의 합을 출력
		System.out.println(s1.length() + s2.length());
	}
	// 공백X 문자열 입력 :: next()
	// 공백O 문자열 입력 :: nextLine()
	// 문자 하나 입력 :: next().charAt(0)	-> 입력받은 문자열 중 첫번째 문자만 추출
}
