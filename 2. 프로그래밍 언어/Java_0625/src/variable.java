
public class variable {
	public static void main(String[] args) {
		// 자료형 :: 정보의 카테고리
		//		JavaScript 자료형 -> number, string, boolean
		
		//	- 정수형(소수점X)	:: byte, short, "int", long (표현 범위 차이)
		//	- 실수형(소수점O)	:: float, "double" (정밀도 차이)
		//	- 문자형 			:: char(문자 하나, ''), String(2개 이상의 문자, "")
		//	- 진위형 			:: boolean (true/false)
		
		// 변수 :: 값을 저장하는 공간
		//	[자료형] [변수이름] = [초기값]
		
		int i = 5;
		double d = 12.34;
		char c = 'a';
		String s = "abc";
		boolean b = true;
		
		// 이름(name), 혈액형(blood), 나이(age), 키(height), 자기소개(intro)
		//	위처럼 변수를 만들고, 임의의 값으로 값 초기화
		//	출력문을 통해서, 5개의 변수값을 출력
		
		String name = "이유나";
		char blood = 'A';
		int age = 35;
		double height = 171.1;
		String intro = "잘 부탁드립니다.";
		
		System.out.println("이름: " + name);
		System.out.println("혈액형: " + blood + "형");
		System.out.println("나이: " + age + "세");
		System.out.println("키: " + height + "cm");
		System.out.println("자기소개: " + intro);
	}

}



