import java.util.Scanner;

abstract class Payment { // 미구현된 메소드를 포함하여, 카드결제/현금결제 공통분모 정의
	// - 필드 :: price(int)
	public int price;
	// - 생성자 :: Payment(int)
	public Payment(int p) {
		this.price = p;
	}
	// - printPrice() :: price값 출력
	public void printPrice() {
		System.out.println("가격: " + this.price);
	}
	// - pay() -> 추상 메소드로 설정
	abstract public void pay();
}
class CardPayment extends Payment {
	// - 생성자 :: CardPayment(int)
	public CardPayment(int pr) {
		super(pr); // Payment 생성자 실행
	}
	public void pay() {
		System.out.println(this.price+"원을 카드로 결제합니다.");
	}
}
class CashPayment extends Payment {
	// - 생성자 :: CashPayment(int)
	public CashPayment(int pr) {
		super(pr); // Payment 생성자 실행
	}
	public void pay() {
		System.out.println(this.price+"원을 현금으로 결제합니다.");
	}
}

public class Ex_pay {
	public static void main(String[] args) {
		// Payment p = new Payment(1500);
		Scanner scan = new Scanner(System.in);
		
		CardPayment cr = new CardPayment(scan.nextInt());
		CashPayment cs = new CashPayment(scan.nextInt());
		
		cr.printPrice();
		cr.pay();
		System.out.println();
		
		cs.printPrice();
		cs.pay();
	}

}
