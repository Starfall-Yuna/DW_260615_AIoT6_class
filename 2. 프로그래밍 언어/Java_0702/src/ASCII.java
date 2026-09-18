
public class ASCII {
	public static void main(String args[]) {
		// 아스키코드, 유니코드(한글) :: 
		// 		사람이 사용하는 기호를 컴퓨터가 인식할 수 있게끔
		//			기호와 숫자를 1대1 대응한 표
//		System.out.println('b');
//		System.out.println((int)'b');
		
		// 'A' = 65
		// 'a' = 97
		// '0' = 48
		for(int i=0; i<10; i++) {
			System.out.println((int)('0'+i));
		}
		for(int i=0; i<26; i++) {
			System.out.println((char)('a'+i));
		}
	}
}
