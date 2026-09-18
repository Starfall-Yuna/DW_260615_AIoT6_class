package Controller;

import java.util.Scanner;

import Service.NumberService;

public class NumberController {
	public static void main(String args[]) {
		while(true) {
			System.out.println("< 실행할 기능을 선택하세요 >");
			System.out.println("1. 숫자 저장");
			System.out.println("2. 계산 결과 출력");
			System.out.println("0. 프로그램 종료");
			System.out.print("선택 :");
			
			Scanner scan = new Scanner(System.in);
			int command = scan.nextInt();
			
			switch(command) {
			case 1:
				NumberService.numberInsert();
				break;
			case 2:
				NumberService.numberCalc();
				break;
			case 0:
				System.out.println("실행을 종료합니다.");
				System.exit(0);
			}
		}
	}
}
