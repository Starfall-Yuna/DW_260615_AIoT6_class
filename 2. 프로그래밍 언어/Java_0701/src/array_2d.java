
public class array_2d {
	public static void main(String args[]) {
		// 2차원 배열 :: 1차원 배열 여러개가 묶인 배열
		// (자료형)[][] (배열이름) = new (자료형) [1차원배열개수][1차원배열크기];
		
		// 3명의 학생의 2과목 점수 입력받고, 각 학생의 점수 평균 내기
		int[][] grade = new int [3][2];
		grade[0][0] = 80;
		grade[0][1] = 70;
		grade[1][0] = 80;
		grade[1][1] = 100;
		grade[2][0] = 50;
		grade[2][1] = 75;
		
		// 중첩 반복문으로 배열값 확인 -> 위의 순서대로 확인
		//	[0][0] -> [0][1] -> [1][0] -> [1][1] -> ...
		
		for(int i=0;i<3;i++) {
			for(int j=0;j<2;j++) {
				System.out.print(grade[i][j]+" ");
			}
			System.out.println();
		}
		
		// 각 학생의 성적 평균을 구하고, 평균이 가장 높은 값을 찾아보세요
		int max = 0;
		for(int i=0;i<3;i++) {
			int sum=0;	// [0]번 학생, [1]번 학생, [2]번 학생
			for(int j=0;j<2;j++) {
				sum += grade[i][j];
			}
			System.out.println(i+"번 학생 평균: "+(sum/2));
			
			if(max < sum/2) {
				max = sum/2;
			}
		}
		System.out.println(max);
	}
}
