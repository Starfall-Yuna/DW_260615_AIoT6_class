import java.util.Scanner;

public class repeat_break {
	public static void main(String args[]) {
		// break :: 반복문 탈출
		Scanner scn = new Scanner(System.in);
		
		int num = scn.nextInt();
		
		for(int i=1; true; i++) {	// 조건식이 true라면(무한 반복문), "일단은 실행한다"를 의미
			// num과 같은 값을 만나면, 출력 중단
			if(i == num) {
				System.out.println("입력값과 동일한 값입니다.");
				break;
			}
			
			
			System.out.println(i);
		} 
		// break 만나면, 여기로 이동
		
		
	}
}
