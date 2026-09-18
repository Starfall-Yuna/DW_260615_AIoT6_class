-- LECTURE 테이블 생성 (4개의 칼럼)
CREATE TABLE LECTURE(
    L_NUM VARCHAR2(10),
    NAME VARCHAR2(50),
    PROF VARCHAR2(30),
    GRADE NUMBER
);

-- 예시 데이터 10개 추가
INSERT INTO LECTURE VALUES ('L001', '데이터베이스 기초', '김민수', 3);
INSERT INTO LECTURE VALUES ('L002', 'Java 프로그래밍', '이서연', 3);
INSERT INTO LECTURE VALUES ('L003', '웹 프로그래밍', '박지훈', 2);
INSERT INTO LECTURE VALUES ('L004', '운영체제', '최유진', 3);
INSERT INTO LECTURE VALUES ('L005', '컴퓨터 네트워크', '정현우', 3);
INSERT INTO LECTURE VALUES ('L006', '인공지능 개론', '한수빈', 2);
INSERT INTO LECTURE VALUES ('L007', '자료구조', '윤도현', 3);
INSERT INTO LECTURE VALUES ('L008', '알고리즘', '오지은', 3);
INSERT INTO LECTURE VALUES ('L009', '정보보안', '강민재', 2);
INSERT INTO LECTURE VALUES ('L010', '소프트웨어 공학', '송하늘', 3);

-- SELECT문
-- SELECT [조회할_칼럼] FROM [테이블명];     (* :: "전체")
SELECT * FROM LECTURE;      -- 모든 칼럼에 대한 LECTURE 데이터 조회

-- AS :: 칼럼에 별명을 붙일 때 사용 (AS를 사용한 SELECT를 사용하는 동안에만 벌명 적용)
--      [칼럼명] AS [별명]       "이 칼럼명을 별명으로 부른다."
SELECT L_NUM AS 강의번호,
    NAME AS 강의명,
    PROF AS 담당교수,
    GRADE AS 권장수강학년
FROM LECTURE;

-- ORDER BY :: 정렬할 때 사용 (오름차순(ASC) 정렬이 기본값, DESC를 통해 내림차순)
--      ORDER BY [정렬_기준이_될_칼럼명] [정렬방법, ASC]
-- GRADE 칼럼을 기준으로, 데이터를 내림차순 정렬
SELECT * FROM LECTURE
    ORDER BY GRADE DESC;
-- NAME 칼럼을 기준으로, 데이터를 오름차순 정렬 (VARCHAR2 데이터 정렬O)
SELECT * FROM LECTURE
    ORDER BY NAME;  
-- GRADE 기준 내림차순 정렬 -> 같은 GRADE 칼럼값을 가진다면 PROF를 오름차순 정렬
SELECT * FROM LECTURE
    ORDER BY GRADE DESC, PROF ASC;

-- 집계 함수 :: SUM(), AVG(), "MAX(), MIN(), COUNT()"
-- COUNT() :: 조건에 맞는 데이터 개수를 세는 함수
--      LECTURE 테이블의 총 데이터 개수를 세어서 표현
SELECT COUNT(*) FROM LECTURE;   -- SELECT * FROM LECTURE;로 나타나는 결과물 개수

SELECT GRADE FROM LECTURE;
SELECT COUNT(GRADE) FROM LECTURE;   -- 결과 :: 10
SELECT
    MAX(GRADE) AS 수강학년_최대,
    MIN(GRADE) AS 수강학년_최소
FROM LECTURE;

-- DISTINCT :: SELECT문의 결과 중 중복된 값을 제거한 값만 제시
SELECT DISTINCT GRADE FROM LECTURE;
-- GRADE 칼럼값의 가짓수를 출력하는 SELECT문 작성  -> 결과 예상값 :: 2
SELECT COUNT(DISTINCT GRADE) AS 권장수강학년_개수
FROM LECTURE;


