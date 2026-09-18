-- SCORE 테이블 활용 문제

-- 1. 자료구조의 점수가 60 이상인 데이터를 조회하고,
-- 	 그 결과에 대한 전체 칼럼을 조회하며, 학생명 기준으로 오름차순 정렬
SELECT * FROM SCORE
    WHERE DATA >= 60
    ORDER BY NAME ASC;

-- 2. 알고리즘의 점수가 90 이상인 데이터를 조회하고,
--	 알고리즘 칼럼에 대해서만 조회하며, 중복값이 없게끔 조회
SELECT DISTINCT ALGO FROM SCORE
    WHERE ALGO >= 90;

-- 3. 네트워크의 점수가 NULL값이 아닌 데이터를 조회하고,
--	 조회된 데이터의 개수를 조회
SELECT COUNT(*) FROM SCORE
    WHERE NETW IS NOT NULL;     -- <>로는 NULL 여부 파악X

