-- 테이블 칼럼 "제약조건" ::
--      칼럼에 넣을 수 있는 값에 제약을 걸어주는 문법

-- 학생 테이블 생성
CREATE TABLE STUDENT(
    NAME VARCHAR2(50) UNIQUE,           -- 학생명(문자열)
    NUM VARCHAR2(30) PRIMARY KEY,       -- 주민등록번호(문자열)
    GENDER VARCHAR2(30) NOT NULL,       -- 성별(문자열, NULL값 삽입X)
    SCORE NUMBER CHECK (0<=SCORE AND SCORE<=100)    -- 성적(숫자)
);
SELECT * FROM STUDENT;

-- 4) CHECK :: "지정된 칼럼에 입력할 수 있는 값의 범위/조건" 설정
INSERT INTO STUDENT VALUES ('Jung', '111111-1111111', '남성', -50);   -- CHECK 칼럼에 조건에 틀리는 값 삽입 시도

-- 3) PRIMARY KEY(PK) :: 식별자 (NOT NULL + UNIQUE)
INSERT INTO STUDENT VALUES ('Park', NULL, '남성', 75);                -- PK 칼럼에 NULL값 삽입 시도
INSERT INTO STUDENT VALUES ('Park', '123456-1234567', '남성', 75);    -- PK 칼럼에 '123456-1234567' 중복값 삽입 시도

-- 2) UNIQUE :: "유일한", 데이터 중복X 
INSERT INTO STUDENT VALUES ('Lee', '123456-1234567', '남성', 50);
INSERT INTO STUDENT VALUES ('Lee', '000000-0000000', '여성', 70);     -- UNIQUE 칼럼에 'Lee' 중복값 삽입 시도

-- 1) NOT NULL :: "지정된 칼럼에 NULL을 삽입X" 제약조건 추가
INSERT INTO STUDENT VALUES ('Lee', '987654-12334567', NULL, 100);     -- NOT NULL 칼럼에 NULL값 삽입 시도




