import java.util.Scanner;

public class Ex_9051 {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		
		// 10개의 정수를 입력받아 그 수들 중 짝수의 개수가 몇 개인지 출력
		int count = 0;	// 짝수의 개수 저장할 변수 생성
		
		for(int i=1; i<=10; i++) {
			int n = scn.nextInt();
			if(n % 2 == 0) { count++; }		// 짝수라면, 개수에 포함 -> if로 표현
		}
		
		System.out.println("입력받은 짝수는 "+count+"개입니다.");
		
//		int n1 = scn.nextInt();
//		if(n1 % 2 == 0) {count++;}
//		int n2 = scn.nextInt();
//		if(n2 % 2 == 0) {count++;}
//		int n3 = scn.nextInt();
//		if(n3 % 2 == 0) {count++;}
//		int n4 = scn.nextInt();
//		if(n4 % 2 == 0) {count++;}
//		int n5 = scn.nextInt();
//		if(n5 % 2 == 0) {count++;}
//		int n6 = scn.nextInt();
//		if(n6 % 2 == 0) {count++;}
//		int n7 = scn.nextInt();
//		if(n7 % 2 == 0) {count++;}
//		int n8 = scn.nextInt();
//		if(n8 % 2 == 0) {count++;}
//		int n9 = scn.nextInt();
//		if(n9 % 2 == 0) {count++;}
//		int n10 = scn.nextInt();
//		if(n10 % 2 == 0) {count++;}
	}
}
