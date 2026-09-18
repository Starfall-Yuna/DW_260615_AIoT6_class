import java.util.Scanner;

public class String_func {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String s = "hello";
		
		// - length() :: 문자열의 길이 제시
		// - charAt(번호) :: 지정된 번호 문자 하나 추출
		System.out.println(s.charAt(1));			// 0번부터 시작
		System.out.println(s.charAt(s.length()-1));	// 문자열의 끝 문자 추출
		
		// - equals(비교할_문자열) :: 두 문자열이 같은지 비교 (같으면 true, 다르면 false 제시)
		//	(ex) ==이 있는데... 왜 굳이 얘를?
		String h = "hello";
		if(s == h) { System.out.println("== 활용 :: s와 h는 같습니다."); }
		String input1 = scan.next();
		if(s == input1) { System.out.println("== 활용 :: s와 input1은 같습니다."); }
		if(s.equals(input1) == true) { 
			System.out.println("equals() 활용 :: s와 input1은 같습니다."); 
		}
		
		// - substring(시작번호, 끝번호) :: 문자열 자르기 (끝번호 이전까지만 슬라이싱)
		System.out.println(s.substring(0, 3));	// 0번~2번 위치 슬라이싱	
	}
}
