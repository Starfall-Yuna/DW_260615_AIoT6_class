import java.util.Scanner;

public class Ex_search {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		// 문제 ::
		//		1) 변수 n을 입력받고, n개의 정수를 저장할 수 있는 배열 생성
		System.out.print("배열의 크기 입력: ");
		int n = sc.nextInt();
		int[] arr = new int [n];	// 배열 번호 :: 0번 ~ n-1번
		
		//		2) n개의 배열값 입력
		System.out.println("배열에 삽입할 값 입력: ");
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		//		3) 임의의 숫자 변수 number 입력
		System.out.print("검색할 값 입력: ");
		int number = sc.nextInt();
		
		//		4) 배열값 중 number값이 존재하는지 여부 출력
		boolean success = false;	// true 찾았다, false 찾지 못했다
		for(int i=0; i<n; i++) {
			if(arr[i] == number) {		// 찾은 경우
				success = true;
			}
		}
		
		if(success == true) {
			System.out.println("검색한 값이 존재합니다.");
		}
		else {
			System.out.println("검색한 값이 존재하지 않습니다.");
		}
	}
}
