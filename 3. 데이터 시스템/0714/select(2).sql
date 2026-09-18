-- 유료강의 테이블 생성 (강의명, 가격, 강사, 총 시수)
CREATE TABLE LECTURE(
    TITLE VARCHAR2(50),
    PRICE NUMBER, 
    TEACHER VARCHAR2(50),
    TOTAL_HOUR NUMBER
);

INSERT INTO LECTURE VALUES ('자바 프로그래밍', 15000, '김민수', 30);
INSERT INTO LECTURE VALUES ('파이썬 데이터 분석', 22000, '이서연', 40);
INSERT INTO LECTURE VALUES ('네트워크 기초', 12000, '박지훈', 20);
INSERT INTO LECTURE VALUES ('SQL 데이터베이스', 18000, NULL, 35);
INSERT INTO LECTURE VALUES ('자바 웹 개발', 25000, '김민수', 50);
INSERT INTO LECTURE VALUES ('토이 프로젝트 제작', 18000, NULL, 25);

SELECT * FROM LECTURE;

-- * 집계 함수 :: MAX(), MIN(), COUNT(), "SUM(), AVG()"
--      SUM() :: 지정된 칼럼값의 총 합계
SELECT
    SUM(PRICE) AS 패키지_가격
FROM LECTURE;
--      AVG() :: 지정된 칼럼값의 평균
--  총 시수 칼럼값의 평균 출력
SELECT
    ROUND(AVG(TOTAL_HOUR), 2) AS 시수_평균
FROM LECTURE;  -- ROUND() :: 실수값의 소수점 표현 조절

-- * WHERE절 :: 데이터 필터링 -> 조건식
--  - 비교연산 ::     =(같다), <>(다르다), 부등호
SELECT * FROM LECTURE
    WHERE TEACHER = '김민수';    -- 강사명이 '김민수'인 데이터만 조회
SELECT * FROM LECTURE
    WHERE TEACHER <> '김민수';   -- 강사명이 '김민수'가 아닌 데이터만 조회 (NULL값 조회X)
SELECT * FROM LECTURE
    WHERE PRICE > 20000;        -- 가격이 20000보다 큰 데이터만 조회
SELECT * FROM LECTURE
    WHERE TOTAL_HOUR <= 30;     -- 총 시수가 30보다 작거나 같은 데이터만 조회
    
--  - NULL 검색 ::   IS NULL, IS NOT NULL
SELECT * FROM LECTURE
    WHERE TEACHER IS NULL;      -- 강사명이 NULL값인 데이터만 조회
SELECT * FROM LECTURE
    WHERE TEACHER IS NOT NULL;  -- 강사명이 NULL값이 아닌 데이터만 조회

-- 논리연산 :: AND(그리고), OR(또는), NOT(~아니다)
SELECT * FROM LECTURE
    WHERE TEACHER='김민수' AND TOTAL_HOUR>=50;
    -- 강사명이 '김민수'이면서(AND) 총 시수가 50 이상인 데이터만 조회 (1개)
SELECT * FROM LECTURE
    WHERE TEACHER='김민수' OR TOTAL_HOUR>=40;
    -- 강사명이 '김민수'이거나(OR) 총 시수가 40 이상인 데이터만 조회 (3개)
SELECT * FROM LECTURE
    WHERE NOT TEACHER='김민수';
    -- 강사명이 '김민수'가 아닌(NOT) 데이터만 조회 (NULL값 조회X)



