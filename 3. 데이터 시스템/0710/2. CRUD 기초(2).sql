-- CRUD (CREATE, READ, UPDATE, DELETE) 기초

-- DDL :: CREATE(생성), ALTER(변경), DROP(삭제), TRUNCATE(삭제)
--      DROP :: 데이터 + 테이블 공간 통째로 삭제
--      TRUNCATE :: 데이터만 삭제
-- DML :: INSERT(삽입), UPDATE(수정), DELETE(삭제)
-- DQL(Query) :: SELECT(조회)

CREATE TABLE EMPLOYEE(  -- 칼럼:: 사원ID, 이름, 급여, 부서
    EMP_ID INT,
    EMP_NAME VARCHAR2(50),
    SALARY NUMBER, 
    DEPARTMENT VARCHAR2(50)
);

-- 사원 테이블에 TEL "칼럼 추가(ADD)"
--                  ADD [추가할_칼럼명] [추가할_칼럼의_데이터 타입]
ALTER TABLE EMPLOYEE ADD TEL VARCHAR2(20);
-- 사원 테이블에 SALARY "칼럼 제거(DROP COLUMN)"
--                  DROP COLUMN [삭제할_칼럼명]
ALTER TABLE EMPLOYEE DROP COLUMN SALARY;
-- 사원 테이블에 DEPARTMENT "칼럼 이름 수정(RENAME COLUMN)"
--                  RENAME COLUMN [기존_칼럼명] TO [변경할_칼럼명]
ALTER TABLE EMPLOYEE RENAME COLUMN DEPARTMENT TO DEP;   -- 칼럼명 DEPARTMENT -> DEP 수정
-- 사원 테이블에 EMP_ID "칼럼 데이터 타입 수정(MODIFY)"
--                  MODIFY [기존_칼럼명] [변경할_데이터 타입]
ALTER TABLE EMPLOYEE MODIFY EMP_ID NUMBER;

SELECT * FROM EMPLOYEE;

INSERT INTO EMPLOYEE VALUES (1, 'Lee', '행정부', '010-0000-0000');
INSERT INTO EMPLOYEE VALUES (2, 'Kim', '교무부', '010-1111-1234');
INSERT INTO EMPLOYEE VALUES (3, 'Jung', '교무부', '010-1234-5678');

-- 사원명이 'JUNG'인 데이터에 대해, 사원ID를 5로 수정한다.
-- UPDATE [테이블명] SET [칼럼명]=[값] (WHERE [행_선택할_조건문])
UPDATE EMPLOYEE SET EMP_ID=5;   -- 전체 데이터의 사원ID를 5로 수정
UPDATE EMPLOYEE SET EMP_ID=5 WHERE EMP_NAME='Jung';

-- 부서명이 '행정부'인 데이터 삭제
-- DELETE FROM [테이블명] (WHERE [행_선택할_조건문])
DELETE FROM EMPLOYEE WHERE DEP='행정부';
-- 사원ID가 2인 데이터 삭제
DELETE FROM EMPLOYEE WHERE EMP_ID=2;
-- EMPLOYEE 테이블 데이터 전체 삭제 (TRUNCATE 동작과 차이O)
DELETE FROM EMPLOYEE;

-- TRUNCATE TABLE [테이블명];
TRUNCATE TABLE EMPLOYEE;
