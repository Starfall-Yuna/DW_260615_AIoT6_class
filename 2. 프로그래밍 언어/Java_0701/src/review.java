
public class review {
	public static void main(String args[]) {
		// 배열 :: 동일한 이름으로 여러 값을 저장
		
//		int[] step = new int [5];	-> 배열 공간 할당
//		step[0] = 100;
//		step[1] = 12000;
		int[] step = {100, 12000, 0, 0, 5000};	// 값 설정+배열 공간 생성 
		System.out.println("총 "+step.length+"일 걸음수가 기록되었습니다.");	// 배열 크기 :: 5
		for(int i=0; i<step.length; i++) {			
			System.out.print(i+"일차: ");
			
			// 배열값 불러오기
			if(step[i] == 0) {
				System.out.println("입력된 값이 없습니다");
			}
			else {
				System.out.println(step[i]+"보");
			}
		}
		System.out.println();
		
		// step 배열값의 최대 최소를 각각 구하여, 이를 출력하라.
		int max = step[0];
		int min = step[0];
		for(int i=1; i < step.length; i++) {
			// 0보(입력값 취급X)인 경우엔, 최대 최소 연산 배제	-> continue
			if(step[i] == 0) {continue;}	// 반복문의 처음으로 (i++; -> 조건문 -> 명령문 수행)
			
			if(max < step[i]) {		// 현재 max보다 더 큰 값 발견
				max = step[i];
			}
			if(min > step[i]) {		// 현재 min보다 더 작은 값 발견
				min = step[i];
			}
		}
		System.out.println("최대 걸음수: "+max);
		System.out.println("최소 걸음수: "+min);
		System.out.println();
		
		int sum = 0;
		for(int i=0; i<step.length; i++) {
			sum += step[i];
			
			// 총 걸음수가 10000보를 넘겼다면, break;
			if(sum >= 10000) {
				System.out.println(i+"일차에 10000보를 넘겼습니다.");
				break;	// 반복문 탈출/종료
			}
		}
		System.out.println("총 걸음수: "+sum);
	}
	// * 무한반복문 :: 조건식에 true 작성, "일단은 실행하게끔" 하는 반복문
	// * 중첩반복문 :: "반복문 안에 반복문"
}



