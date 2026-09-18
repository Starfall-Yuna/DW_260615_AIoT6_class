import java.util.Scanner;

public class Ex_9063 {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		// 5개의 정수를 입력받은 후 차례로 출력
		int[] arr = new int [5];
		for(int i=0; i<5; i++) {
			arr[i] = sc.nextInt();
		}
		// arr[0], arr[1], arr[2], arr[3], arr[4]
		for(int i=0; i<5; i++) {
			System.out.print(arr[i]+" ");
		}
	}
}
