import java.util.Scanner;

public class condition {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		// - 비교연산자 :: <, >, <=, >=, ==(같다), !=(다르다)
		// - 논리연산자 :: &&(and), ||(or), !(not)
		
		// 조건문 :: 특정 조건을 만족할 때, 수행할 명령어 작성
		// if - else if - else (if :: 독립적으로 사용O)
		int age = scan.nextInt();
		if(19<=age && age<=34) {
			System.out.println("당신은 청년입니다.");
		}
		else if(age<19) {
			System.out.println("당신은 미성년자입니다.");
		}
		else {
			System.out.println("당신은 청년이 아닙니다.");
		}
		
		boolean ok = scan.nextBoolean();
		if(ok == true) {
			System.out.print("성공적으로 종료되었습니다.");
		}
	}
}
