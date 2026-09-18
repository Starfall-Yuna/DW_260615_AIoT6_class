-- [대학교] "여러 교수님이 하나의 강의를 진행할지?"
-- [대학교] "여러 강의를 하나의 교수님이 진행할지?" (O)
--      => "여러 개"에 속하는 테이블에 FK를 지정하는 게 자연스러움
--      => LECTURE에 FK 설정
CREATE TABLE LECTURE(
    LECTURE_ID VARCHAR2(10) PRIMARY KEY,    -- LECTURE의 식별자
    TITLE VARCHAR2(50), 
    PROF_ID VARCHAR2(10),
    MAJOR VARCHAR2(30),
    -- 외래키(FK) :: 테이블 연결 (칼럼을 하나씩 골라 연결)
    FOREIGN KEY (PROF_ID)
        REFERENCES PROF(PROF_ID)    -- 이 테이블의 칼럼이, PROF.PROF_ID 참조
);
CREATE TABLE PROF(
    PROF_ID VARCHAR2(10) PRIMARY KEY,       -- PROF의 식별자
    NAME VARCHAR2(30),
    AGE NUMBER
);
-- LECTURE.PROF_ID - PROF.PROF.ID 연결

-- 실행 순서 :: PROF 생성/데이터 삽입 -> LECTURE 생성/데이터 삽입
INSERT INTO PROF VALUES ('P001', 'Lee', 35);
INSERT INTO PROF VALUES ('P002', 'Kim', 55);

INSERT INTO LECTURE VALUES ('L001', 'JAVA프로그래밍', 'P001', '컴공');
INSERT INTO LECTURE VALUES ('L002', 'C프로그래밍', 'P001', '컴공');
INSERT INTO LECTURE VALUES ('L003', '교육심리', 'P002', '사범');
INSERT INTO LECTURE VALUES ('L004', '교육행정', 'P002', '사범');

SELECT * FROM PROF;
SELECT * FROM LECTURE;

SELECT *
FROM LECTURE, PROF;     -- LECTURE 4개 데이터 * PROF 2개 데이터 = 8가지 데이터

SELECT *
FROM LECTURE L, PROF P
WHERE L.PROF_ID = P.PROF_ID;    -- 위 조회한 8개 결과에서, PROF_ID끼리 같은 데이터만(WHERE) 조회   -> 4가지 데이터

-- 'JAVA프로그래밍' 강의 데이터와 이를 진행하는 교수 데이터 조회
SELECT *
FROM LECTURE L, PROF P
WHERE L.PROF_ID = P.PROF_ID AND
    L.TITLE = 'JAVA프로그래밍';
    
-- [참고] 서브쿼리 :: SELECT문 안의 SELECT문
--      집계 함수랑 같이 활용
SELECT *
FROM LECTURE L, PROF P
WHERE L.PROF_ID = P.PROF_ID AND
    L.LECTURE_ID = (        -- L.LECTURE_ID = 'L001'
        SELECT LECTURE_ID
        FROM LECTURE L
        WHERE L.TITLE = 'JAVA프로그래밍'
);