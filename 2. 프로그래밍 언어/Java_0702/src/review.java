import java.util.Arrays;
import java.util.Collections;

public class review {
	public static void main(String args[]) {
		// * 2차원 배열
		// 여러 개의 변수를 하나의 이름으로 -> 1차원 배열
		// 여러 1차원 배열을 하나의 이름으로 -> 2차원 배열

		// [a][b] -> a번째 배열의 b번째 값
		int[][] salescount = { 
			{ 12, 15, 10, 18, 20 }, 	// 0번 메뉴의 0~4일차 간의 판매수 (0번 배열의 5개 값)
			{ 8, 10, 7, 5, 0 }, 		// 1번 메뉴의 0~4일차 간의 판매수
			{ 5, 4, 9, 10, 1 } 			// 2번 메뉴의 0~4일차 간의 판매수
		};
		// int[][] salescount = new int [3][5];
		
		// 2중 반복문 활용해서 2차원 배열 출력
		for(int i=0; i<3; i++) {		// 몇번 배열로 들어갈지 
			System.out.println(i+"번 메뉴 일별 판매량: ");
			for(int j=0; j<5; j++) {		// 몇번 값으로 들어갈지
				System.out.print(salescount[i][j]+"\t");
			}
			System.out.println();
		}
		
		// * 0~2번 메뉴 중, 총 판매량의 최댓값 찾기
		int max = 0;
		for(int i=0; i<3; i++) {
			int sum = 0;	// i=0 -> 0번 메뉴의 판매량 총합 저장
			for(int j=0; j<5; j++) {
				sum += salescount[i][j];	// i=0 -> 0번 메뉴의 0일차~4일차 값을 sum 가산
			}
			
			// 3가지의 sum값 중 최댓값을 max에 저장하고, 이를 출력
			if(max < sum) {max = sum;}
		}
		System.out.println("BEST메뉴 판매량: "+max);
		// System.out.println(salescount);
		
		// Arrays.sort(salescount);
		// 위 정렬 기능 활용하고, 뒤에서부터 앞으로 출력
	}
	// 함수 기능 :: length, Arrays.toString(배열이름), Arrays.sort(배열이름)
}




