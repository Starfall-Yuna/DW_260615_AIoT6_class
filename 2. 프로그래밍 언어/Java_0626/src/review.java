import java.util.Scanner;

// Java에서는, 명령문 마지막에 반드시 ;(세미콜론) 붙여야 함
public class review {
	// main 함수 :: 파일 실행할 때, 가장 먼저 찾아서 실행하는 함수
	public static void main(String[] args) {
		// * 출력문 :: print(), println(), printf()
		// * 입력문 :: Scanner 활용
		// * 자료형 ::
		// 정수형(byte, short, "int", long), 실수형(float, "double")
		// 문자형(char, String), 진위형(boolean)

		Scanner scan = new Scanner(System.in); // 입력문 작성 시, Scanner 활용

		// 콘솔을 통해 사용자에게 나이, 키(m), 몸무게(kg) 입력
		System.out.print("나이를 입력하세요: ");
		int age = scan.nextInt();
		System.out.print("키(m)를 입력하세요: ");
		double height = scan.nextDouble();
		System.out.print("몸무게(kg)를 입력하세요: ");
		double weight = scan.nextDouble();

		// 입력값을 사용자에게 콘솔로 출력
		// 나이(age), 키(height), 몸무게(weight)
		System.out.println(); // 줄바꿈("\n") 수행 = System.out.print("\n");
		System.out.println("나이: " + age + "세");
		System.out.println("키: " + height + "m");
		System.out.println("몸무게: " + weight + "kg");

		// 입력값에 대한 bmi값을 연산해서 사용자에게 출력
		// 변수 생성 :: [자료형] [변수이름];
		// 값 설정 :: [변수명] = [값];
		// 변수 초기화 :: [자료형] [변수이름] = [값];
		double bmi = weight / (height * height);
			// double bmi;	+	bmi = weight / (height * height);
		System.out.println("bmi 결과: " + bmi);
	}

}





