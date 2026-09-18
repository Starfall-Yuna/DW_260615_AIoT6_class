import java.util.Scanner;

public class find_max {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		// 입력한 배열값 중, 가장 큰 값 구하기
		
		int[] num = new int [10];
		for(int i=0; i<10; i++) {
			num[i] = sc.nextInt();	// num[0]~num[9] 입력
		}
		
		int max=num[0];		// 최댓값 저장
		for(int i=1; i<10; i++) {	
			if(max < num[i]) {
				max = num[i];
			}
		}
		System.out.println(max);
	}
}
