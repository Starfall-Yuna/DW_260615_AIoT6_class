-- * SCORE 테이블 생성
CREATE TABLE SCORE(
    NAME VARCHAR2(30),
    ALGO NUMBER,
    DATA NUMBER,
    NETW NUMBER
);

-- * 예시 데이터 생성 (4개)
INSERT INTO SCORE VALUES ('Lee', 90, 80, 70);
INSERT INTO SCORE VALUES ('Park', 100, 50, 60);
INSERT INTO SCORE VALUES ('Kim', 70, 75, 70);
INSERT INTO SCORE VALUES ('Yun', 60, 80, 90);

-- *  전체 SCORE 데이터 조회
SELECT 
    NAME AS 학생명,
    ALGO AS 알고리즘,
    DATA AS 자료구조,
    NETW AS 네트워크
FROM SCORE;

-- * NAME 칼럼 기준으로 오름차순 정렬 수행
SELECT * FROM SCORE
    ORDER BY NAME ASC;

-- * 전체 데이터 개수 조회   -> COUNT()
SELECT COUNT(*) FROM SCORE;

-- * 알고리즘, 자료구조, 네트워크 점수의 최댓값을 하나의 SELECT문으로 조회
SELECT
    MAX(ALGO) AS 알고리즘_최대,
    MAX(DATA) AS 자료구조_최대,
    MAX(NETW) AS 네트워크_최대
FROM SCORE;

-- * 알고리즘, 자료구조, 네트워크 점수의 최솟값을 하나의 SELECT문으로 조회
SELECT
    MIN(ALGO) AS 알고리즘_최소,
    MIN(DATA) AS 자료구조_최소,
    MIN(NETW) AS 네트워크_최소
FROM SCORE;




