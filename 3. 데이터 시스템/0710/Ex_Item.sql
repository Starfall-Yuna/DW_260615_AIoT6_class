-- 1) 상품(ITEM) 테이블 생성
CREATE TABLE ITEM(
    ITEM_ID INT,
    NAME VARCHAR(50),       -- NAME 칼럼에 넣을 수 있는 데이터 한도 50바이트
    PRICE NUMBER,
    DISCOUNT_PRICE NUMBER, 
    UPLOAD_DATE DATE        -- DATE 데이터 타입 :: 날짜 데이터 형식   
);

-- 2) 위 테이블에 예시 데이터 5가지 삽입
INSERT INTO ITEM VALUES (1, '발라서 쓰는 세제', 2500, 2000, '2026-07-10');
INSERT INTO ITEM VALUES (2, '2026 플래너', 15000, 12000, '2026-01-01');
INSERT INTO ITEM VALUES (3, '에티오피아 원두 1KG', 14000, 13500, '2026-06-30');
INSERT INTO ITEM VALUES (4, '블루투스 이동형 마이크', 80000, 68000, '2026-06-15');
INSERT INTO ITEM VALUES (5, '아두이노 입문용 키트', 42000, 40000, '2026-03-05');

-- 3) 테이블 전체 데이터 조회
SELECT * FROM ITEM;