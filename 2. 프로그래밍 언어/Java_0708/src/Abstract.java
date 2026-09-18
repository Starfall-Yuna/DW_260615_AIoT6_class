// 구체적으로 정의된 클래스만 작성해왔음 -> 그 클래스들로 인스턴스 생성 문제X

// abstract class :: "추상 클래스" -> 인스턴스 생성 불가

abstract class shape{
	public String color;
	
	abstract public void draw();	// "추상 메소드" :: 실행할 명령어(정의부)X
		// 추상 메소드의 실행 동작은, 자식 클래스에게 넘김
	public void printInfo() {		// 구체적으로 정의된 메소드 :: 선언부 + 정의부
		System.out.println("색상: "+this.color);
	}
}
class square extends shape{		
	// "추상 메소드 draw() 구체적으로 정의하라" -> 오버라이딩
	public int width;
	
	public void draw() {	// 추상 메소드 구체화
		System.out.println("정사각형을 그립니다.");
	}
	public void printInfo() {
		System.out.println("색상: "+this.color);
		System.out.println("너비: "+this.width);
	}
}


public class Abstract {
	public static void main(String[] args) {
		// shape s = new shape();	-> 에러 :: 인스턴스화X
		
		square sq = new square();
		sq.draw();
	}

}



