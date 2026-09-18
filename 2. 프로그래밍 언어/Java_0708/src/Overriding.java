
// 오버라이딩 :: (상속 전제) 부모 메소드를 자식이 "재정의" (덮어쓰기X)
//		"Cry() 호출할 때, 부모보다 자식(본인)의 것을 우선시하여 사용"
//		=> 부모 클래스의 "이름, 매개변수 구성 동일한 메소드"를 자식 클래스에서 재정의

class Animal{
	public void Cry() {
		System.out.println("동물이 웁니다.");
	}
}
class Dog extends Animal{
	public void Cry() {
		super.Cry();	// "Dog의 부모인 Animal의 Cry() 호출"
		System.out.println("월월");
	}
}
class Cat extends Animal{
	public void Cry() {
		super.Cry();	// "Cat의 부모인 Animal의 Cry() 호출"
		System.out.println("애옹");
	}
}

public class Overriding {
	public static void main(String[] args) {
		Animal a = new Animal();
		a.Cry();
		System.out.println();
		
		Dog d = new Dog();
		d.Cry();
		System.out.println();
		
		Cat c = new Cat();
		c.Cry();
		// d와 c를 통해서, animal 클래스의 Cry() 실행?	-> O
	}

}
