-- BUILDING(건물) 테이블 생성
CREATE TABLE BUILDING(
    BUILD_ID VARCHAR2(20) PRIMARY KEY,
        -- VARCHAR, 기본키
    CLASS_ID VARCHAR2(20) NOT NULL,
    FOREIGN KEY (CLASS_ID)
        REFERENCES CLASSROOM(CLASS_ID)
        -- "이 테이블의 CLASS_ID 칼럼은 강의실 테이블의 CLASS_ID 칼럼 "참조"
        -- VARCHAR, NULL값 삽입X, CLASSROOM의 동일 칼럼값 참조(FK)
);
-- CLASSROOM(강의실) 테이블 생성
CREATE TABLE CLASSROOM(
    CLASS_ID VARCHAR2(20) PRIMARY KEY,
        -- VARCHAR, 기본키
    CLASS_NAME VARCHAR2(50) UNIQUE,
        -- VARCHAR, 중복값 삽입X
    MAX_PEOPLE NUMBER CHECK (5 <= MAX_PEOPLE AND MAX_PEOPLE <= 50),
        -- NUMBER, 5 이상 50 이하 값만 삽입O
    FLOOR NUMBER CHECK (1 <= FLOOR AND FLOOR <= 5)                          
        -- NUMBER, 1 이상 5 이하 값만 삽입O
);

-- * 실행 순서 & 데이터 생성 순서
--  => BUILDING의 칼럼에 CLASSROOM의 칼럼을 참조하게끔 FK 설정됨
--      (1) 의존받는 CLASSROOM 테이블 생성 & CLASSROOM 테이블 데이터 생성
--      (2) 의존하는 BUILDING 테이블 생성 & BUILDING 테이블 데이터 생성

INSERT INTO CLASSROOM VALUES ('001', '본관201호', 30, 2);
INSERT INTO CLASSROOM VALUES ('002', '본관203호', 25, 2);
INSERT INTO CLASSROOM VALUES ('003', '본관501호', 30, 5);
INSERT INTO CLASSROOM VALUES ('004', '본관502호', 30, 5);
INSERT INTO CLASSROOM VALUES ('005', '본관503호', 25, 5);

INSERT INTO BUILDING VALUES ('DW', '001');
INSERT INTO BUILDING VALUES ('DW', '002');      -- 'DW' 중복된 값X
    -- 설계 잘못X, "같은 건물 데이터에 여러 강의실 배정(1:N관계) -> 이 설계로는 1:N 성립X"
    --  테이블 간의 관계(1:N, N:1, N:M)를 고민하면서, 제약조건 걸어야 함.

SELECT * FROM CLASSROOM;
SELECT * FROM BUILDING;

