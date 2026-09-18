import java.util.Scanner;

public class Ex_9041 {
	public static void main(String args[]) {
		// 점수를 입력받아 80점 이상이면 합격메시지를 그렇지 않으면 불합격 메시지를 출력하는 "작업을 반복"
		// 0~100점 이외의 점수가 입력되면 종료
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			System.out.print("점수를 입력하세요. ");
			int score = sc.nextInt();
			
			if(!(0<=score && score<=100)) {	// 0~100 범위 밖의 입력이라면
				break;
			}
			
			if(score >= 80) {
				System.out.println("축하합니다. 합격입니다.");
			}
			else if(score < 80) {
				System.out.println("죄송합니다. 불합격입니다.");
			}
		}
	}
}
