-- 테이블 제약조건 :: "테이블에 삽입할 데이터에 제약을 둔다"
--      NOT NULL, UNIQUE, CHECK, PK(PRIMARY KEY)

-- 환자 테이블
CREATE TABLE PATIENT(
    NAME VARCHAR2(50) PRIMARY KEY,
        -- 환자명 (2개)
    DOCTOR_ID VARCHAR2(50) NOT NULL,
        -- 담당 의료진 ID (1개)
    DEPART VARCHAR2(50) CHECK (DEPART IN ('내과', '이비인후과', '피부과')),
        -- 진료과 (1개)
    AGE NUMBER CHECK (AGE BETWEEN 1 AND 150)
        -- 나이 (1개)
);

-- 제약조건에 이름 붙이는 방법 (개별적으로 검색, CONSTRAINT)

-- PRIMARY KEY :: NOT NULL + UNIQUE
-- NOT NULL :: NULL값 삽입X 제약
-- CHECK :: 삽입O 값에 조건을 걸어줌 (NULL값 삽입O)
-- UNIQUE :: 중복된 값 삽입X 제약 (NULL값 삽입O)
INSERT INTO PATIENT VALUES ('Lee', 'D001', '이비인후과', 35);
INSERT INTO PATIENT VALUES ('Park', 'D002', NULL, NULL);
INSERT INTO PATIENT VALUES ('Kim', 'D001', '내과', 40);

SELECT * FROM PATIENT;



