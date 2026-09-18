
public class double_repeat {
	// 중첩 반복문 :: "반복문 안에 반복문"
	public static void main(String args[]) {
		for(int i=1; i<10; i++) {
			// i=1) j=1~9
			// i=2) j=1~9 ...
			
			System.out.println(i+"단)");
			for(int j=1; j<10; j++) {	// i값이 변동될때마다 새롭게 생성
				System.out.println(i+"*"+j+"="+(i*j));
			}
			System.out.println();
			
			// System.out.println(j);	// j 변수 존재X
		}
		// System.out.println(i);	// i 변수 존재X
	}
}
