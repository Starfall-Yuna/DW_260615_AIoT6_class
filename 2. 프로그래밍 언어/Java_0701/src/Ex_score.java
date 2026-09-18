import java.util.Arrays;
import java.util.Scanner;

public class Ex_score {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		// 1) 10개 정수를 저장할 수 있는 배열 생성
		int[] score = new int [10];
		
		// 2) 배열값 10개 입력
		for(int i=0; i<10; i++) {
			score[i] = sc.nextInt();
		}
		
		// 3) 10개의 값을 확인하면서, 60 미만 값은 0으로 값 변경하기
		for(int i=0; i<10; i++) {
			if(score[i] < 60) {
				score[i] = 0;
			}
		}
		
		// 4) 배열값 출력
		//		Arrays.toString(배열이름) 활용 (어렵다면, 반복문 활용 출력)
		System.out.println(Arrays.toString(score));
	}
}	




