import java.util.Scanner;

public class break_continue {
	public static void main(String args[]) {
		// * 무한 반복문  (조건식에 true를 작성, "일단은 실행함")
		//		=> 중단점 설정(break)은 필요함
		// break :: 반복문 탈출/종료
		// continue :: 반복문의 처음으로 이동
		Scanner sc = new Scanner(System.in);
		
		while(true) { // continue를 만나면, 여기로 이동
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			// 0 0을 입력받을 때, 실행을 중단
			if(a==0 && b==0) {
				System.out.println("실행을 종료합니다.");
				break;
			}
			// 음수 입력받으면, 입력 다시 받기
			else if(a<0 || b<0) {
				continue;
			}
			
			System.out.println("덧셈 결과: "+(a+b));
		}
		// while에서 break를 만나면, 여기로 이동
	}
}



