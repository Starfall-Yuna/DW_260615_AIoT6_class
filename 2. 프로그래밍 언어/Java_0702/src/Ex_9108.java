import java.util.Scanner;

public class Ex_9108 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		// 문자 하나를 입력 받아서 그 문자의 아스키 코드를 출력하는 작업을 반복
		while(true) {
			char ch = scan.next().charAt(0);
			
			// a -> 97 
			System.out.println(ch+" -> "+(int)ch);
			
			// ‘0’이 입력되면 아스키 코드를 출력하고 종료
			if(ch == '0') {
				break;
			}
		}
	}
}
