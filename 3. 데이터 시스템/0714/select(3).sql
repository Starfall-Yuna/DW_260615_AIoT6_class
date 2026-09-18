-- 상품 테이블 생성 (3개의 칼럼)
CREATE TABLE PRODUCT(
    NAME VARCHAR2(100),
    PRICE NUMBER,
    CATEGORY VARCHAR2(50)
);

INSERT INTO PRODUCT VALUES ('무선 마우스', 25000, '전자기기');
INSERT INTO PRODUCT VALUES ('기계식 키보드', 79000, '전자기기');
INSERT INTO PRODUCT VALUES ('스프링 노트', 3500, '문구');
INSERT INTO PRODUCT VALUES ('텀블러', 18000, '생활용품');
INSERT INTO PRODUCT VALUES ('운동화', 65000, '의류');

SELECT * FROM PRODUCT;

-- [칼럼명] BETWEEN [1] AND [2] :: 범위 지정하여 필터링 (숫자)
--      지정된 칼럼의 값이 [1]~[2] 사이인 데이터 필터링
SELECT * FROM PRODUCT
    WHERE PRICE BETWEEN 20000 AND 80000;

-- [칼럼명] IN (값1, 값2, ...) :: 범위 지정하여 필터링 (숫자, 문자열)
--      지정된 칼럼의 값이 () 안에 있는 값인 데이터 필터링
SELECT * FROM PRODUCT
    WHERE CATEGORY IN ('문구', '생활용품');

INSERT INTO PRODUCT VALUES ('전자식 키보드', 100000, '전자기기');
INSERT INTO PRODUCT VALUES ('정축 키보드', 120000, '전자기기');
INSERT INTO PRODUCT VALUES ('무선 키보드', 80000, '전자기기');
SELECT * FROM PRODUCT;

-- LIKE (%랑 같이 사용) :: 문자열 부분일치 검색
SELECT * FROM PRODUCT
    WHERE NAME LIKE '%키보드';     -- NAME 칼럼값의 마지막이 '키보드'인 값 필터링
SELECT * FROM PRODUCT
    WHERE NAME LIKE '무선%';       -- NAME 칼럼값의 시작이 '무선'인 값 필터링
