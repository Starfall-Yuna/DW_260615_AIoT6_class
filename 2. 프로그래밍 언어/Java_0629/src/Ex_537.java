import java.util.Scanner;

public class Ex_537 {
	public static void main(String args[]) {
		// https://jungol.co.kr/problem/537
		// while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int i=1;
		int sum=0;
		while(i<=n) {
			sum += i;
			System.out.println(sum);
			i++;
		}
	}
}




