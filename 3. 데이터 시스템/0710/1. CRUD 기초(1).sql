-- DDL(Definition, 데이터 정의어) :: 데이터 구조(테이블) "정의" 명령어
-- CREATE TABLE :: 테이블 생성
CREATE TABLE STUDENT(   -- STUDENT 테이블 생성 (4개 칼럼 정의)
    ID VARCHAR2(20),    -- ID 칼럼을 VARCHAR2(20) 타입으로 정의
    NAME VARCHAR2(50),
    GRADE INT,              
    MAJOR VARCHAR2(50)
);

-- DML(Manipulation, 데이터 조작어) :: 데이터 구조(테이블) 내부 "조작" 명령어
-- INSERT :: 테이블에 데이터 삽입
-- INSERT INTO [테이블명] (칼럼1, 칼럼2, ...) VALUES (값1, 값2, ...);
INSERT INTO STUDENT (NAME, MAJOR) VALUES ('JANG', '국어국문학과');    -- ID, GRADE 칼럼은 null값으로 설정
INSERT INTO STUDENT VALUES ('1619', 'Lee', 4, '컴퓨터공학과');        -- 테이블 생성할 시 칼럼이 정의된 순서대로 값 삽입
INSERT INTO STUDENT VALUES ('1813', 'Park', 3, '전자공학과');
INSERT INTO STUDENT VALUES ('2088', 'Kim', 1, '컴퓨터교육과');
INSERT INTO STUDENT (MAJOR, GRADE, ID, NAME) VALUES ('영어교육과', 4, '1111', 'KANG');

-- SELECT :: 테이블 데이터 조회(검색)
-- SELECT [출력할_칼럼명] FROM [테이블명];
-- SELECT NAME, MAJOR FROM STUDENT;
SELECT * FROM STUDENT;      -- * :: "전체"

-- DROP :: 테이블 전체 삭제
-- DROP TABLE [테이블명];
DROP TABLE STUDENT;