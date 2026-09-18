import java.util.Scanner;

public class Ex_9112 {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		// 문자열을 입력받아서
		String input = sc.next();
		
		// 문자열의 길이를 구하고
		System.out.println("입력받은 문자열의 길이는 "+input.length()+"입니다.");
		
		// 입력받은 역순으로 출력
		for(int i=input.length()-1; i>=0; i--) {
			System.out.print(input.charAt(i));
		}
	}
}
