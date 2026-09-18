
class Shape{
	// - 필드 :: color(String)
	public String color;
	// - 생성자 :: Shape(String)
	public Shape(String c) {
		this.color = c;
	}
	
	// - 메소드 :: draw(), printInfo(), Setting()
	public void draw() {
		System.out.println("도형을 그립니다.");
	}
	public void printInfo() {
		System.out.println("색상: "+this.color);
	}
	public void Setting() {
		System.out.println("도형 설정을 시작합니다.");
	}
}
class Square extends Shape{
	// - 필드 :: "color(String)", width(int)
	public int width;
	// - 생성자 :: Square(String, int)
	public Square(String cr, int w) {
		// super() -> 부모 생성자 실행
		super(cr);
		this.width = w;
	}
	
	// - 메소드 :: draw(), printInfo(), Setting(int)
	//		"오버라이딩"을 통해, 부모의 메소드와 다르게 작동하게끔 재정의
	public void draw() {
		System.out.println("정사각형을 그립니다.");
	}
	public void printInfo() {
		System.out.println("색상: "+this.color);
			// super.printInfo() 대체 (부모의 printInfo() 수행)
		System.out.println("너비: "+this.width);
	}
	public void Setting(int cw) {
		this.width = cw;
		System.out.println("변경된 변의 크기: "+this.width);
	}
}

public class Ex_Shape {

	public static void main(String[] args) {
		Shape s = new Shape("Red");
		Square sq = new Square("Blue", 5);
		
		s.draw();
		s.printInfo();
		sq.draw();
		sq.printInfo();
	}

}