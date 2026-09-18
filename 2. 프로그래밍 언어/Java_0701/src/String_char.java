import java.util.Scanner;

public class String_char {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		// char :: 문자 하나('') 
		// String :: 문자열("")
		
		// nextLine() :: 공백O 문자열 입력
//		String st = sc.nextLine();
//		System.out.println(st);
		// next() :: 공백X 문자열 입력
		String s = sc.next();		// "hello world" 입력 -> world 값은 소멸
		System.out.println(s);
		
		System.out.println(s.charAt(1));
		
		// next().charAt(0) :: 문자 하나 입력
		char ch = sc.next().charAt(0);
		System.out.println(ch);
	}
}
