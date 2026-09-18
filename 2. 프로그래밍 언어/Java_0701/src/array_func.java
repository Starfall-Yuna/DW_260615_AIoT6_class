import java.util.Arrays;

public class array_func {
	public static void main(String args[]) {
		double[] a = {85.6, 41.2, 90.2, 77.8};
		
		// length :: 배열의 길이/크기 제시
		System.out.println("배열의 크기: "+a.length);
		// Arrays.toString(배열이름) :: 특정 배열의 내용을 문자열(String) 바꾸어줌
		System.out.println(Arrays.toString(a));
		
		// Arrays.sort(배열이름) :: 배열값들을 오름차순 정렬/정리
		Arrays.sort(a);		// 정렬 수행
		System.out.println(Arrays.toString(a));	// 앞에서 정렬된 결과 출력
	}
}
