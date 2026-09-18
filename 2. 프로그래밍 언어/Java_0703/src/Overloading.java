
public class Overloading {
	// 문법적으로, 같은 이름의 변수/함수 생성X	-> 같은 이름으로는 한번씩만 생성
	
	// 메소드(함수) 오버로딩 (매개변수)
	// 	=> "동일한 이름의 함수라도, 매개변수의 구성을 다르게 하면 함께 사용 가능"
	public static int plus() 		{ return 1+1; }				// 1
	public static int plus(int num) { return num+1; }			// 2
	public static double plus(double num) { return num+1; }		// 3, 매개변수 타입 다름
	public static int plus (int n1, int n2) { return n1+n2; }	// 4, 매개변수 개수 다름
	
	public static void main(String args[]) {
		plus(2.4);		// 3번 함수 실행
		plus(5, 6);		// 4번 함수 실행
		plus();			// 1번 함수 실행
		// plus(5, 6, 7, 8);	// 에러, 함수 구현X
	}
}
