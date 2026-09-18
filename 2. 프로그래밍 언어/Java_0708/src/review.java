
// 상속(extends) :: "부모 클래스의 멤버를 자식 클래스에 물려준다."
//	+ super() :: 생성자?
// String :: 클래스 기반 자료형

class Person{	// 사람 클래스
	// - 필드 :: 이름, 주민번호
	public String name;	
	public String number;
	public Person(String n, String num) {
		this.name = n;
		this.number = num;
	}
}
class Student extends Person{	// 학생 클래스
	// - 필드 :: 이름, 주민번호, 학번, 성적
	public int stu_num;
	public int score;
	public Student() {
		super(null, null);		// name과 number를 null값으로
		this.stu_num = 0;
		this.score = 0;
	}
}
class Teacher extends Person{	// 교사 클래스
	// - 필드 :: 이름, 주민번호, 교사번호, 기술스택
	public int tc_num;
	public String[] stack;	// String형 배열의 멤버 (여러 값 삽입O)
	public Teacher(String n, String num, int tn, int size) {
		super(n, num);			// name, number는 매개변수 값으로
		tc_num = tn;
		stack = new String [size];	
			// "stack 멤버에는, size 개수만큼의 String값을 저장할 수 있다"
	}
}

public class review {
	public static void main(String args[]) {
		Student s = new Student();
		// s.tc_num = 1;
		System.out.println("학생 이름(상속): "+s.name);
		System.out.println("학번: "+s.stu_num);
		System.out.println();
		
		Teacher t = new Teacher("Lee", "000000-0000000", 1, 5);
		System.out.println("교사 주민번호(상속): "+t.number);
		System.out.println("기술스택 저장 개수: "+t.stack.length);
		// t.stu_num = 2;
	}
}




