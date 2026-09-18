
public class func_return {
	// "반환하다"(return) ::
	//		빌려 오거나 차지하였던 것을 본래의 주인이나 상태로 되돌려 주다
	//		
	
	// 
	public static int add(int n) {
		return n+1;
	}
	
	public static void main(String args[]) {
		System.out.println(add(5));		// 6이라는 결과를 받음
			// add(5);	
			//	-> 5라는 값을 add() 함수에 빌려주고, 5+1 결과를 돌려받았음.
	}
}
