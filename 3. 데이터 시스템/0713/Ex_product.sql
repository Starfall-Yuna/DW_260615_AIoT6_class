-- 상품(PRODUCT) 테이블 생성
CREATE TABLE PRODUCT(   -- (상품번호, 상품명, 카테고리, 가격, 재고)
    P_NUM VARCHAR2(10),
    P_NAME VARCHAR2(30),
    CATEGORY VARCHAR2(20),
    PRICE NUMBER,
    STOCK NUMBER
);

-- 카테고리 칼럼값은 겹치는 게 있게끔 데이터 설정
-- 예시 데이터 10개 준비하기 
INSERT INTO PRODUCT VALUES ('1', '스타벅스 10000원권', '기프티콘', 9500, 100);
INSERT INTO PRODUCT VALUES ('2', '적외선 레이저 포인터', '전자기기', 15000, 20);
INSERT INTO PRODUCT VALUES ('3', '블루투스 마우스', '전자기기', 12000, 50);
INSERT INTO PRODUCT VALUES ('4', '500ml 텀블러', '생활용품', 10000, 42);
INSERT INTO PRODUCT VALUES ('5', '배달의민족 3만원권', '기프티콘', 28000, 150);
INSERT INTO PRODUCT VALUES ('6', '0.28 굵기 검정색 볼펜', '필기구', 1800, 200);
INSERT INTO PRODUCT VALUES ('7', '2026 신년 플래너', '필기구', 23000, 10);
INSERT INTO PRODUCT VALUES ('8', '플라스틱 덮개', '생활용품', 2500, 30);
INSERT INTO PRODUCT VALUES ('9', '파리바게뜨 케이크', '기프티콘', 32000, 80);
INSERT INTO PRODUCT VALUES ('10', '지우개 10개입', '필기구', 7500, 30);

-- 1. 전체 데이터 조회 (전체 칼럼)
SELECT * FROM PRODUCT;

-- 2. 전체 데이터 조회 (상품명(P_NAME), 카테고리(CATEGORY), 가격(PRICE))
SELECT 
    P_NAME AS 상품명,
    CATEGORY AS 분류,
    PRICE AS 가격
FROM PRODUCT;

-- 3. 전체 데이터 조회 (재고가 많은 순(내림차순)으로, 재고가 같다면 가격이 저렴한 순(오름차순)으로)
SELECT * FROM PRODUCT
    ORDER BY STOCK DESC, PRICE;

-- 4. 카테고리의 고유값을 조회 (중복값 제거 -> DISTINCT)
SELECT DISTINCT CATEGORY FROM PRODUCT;

-- 5. 카테고리의 가짓수를 조회 -> COUNT()
SELECT 
    COUNT(DISTINCT CATEGORY) AS 분류_가짓수
FROM PRODUCT;

-- 6. 전체 상품 수를 조회
SELECT COUNT(*) FROM PRODUCT;

-- 7. 가장 큰 재고 데이터 출력
-- 8. 가장 저렴한 가격 데이터 출력
SELECT 
    MAX(STOCK) AS 재고_최대값,
    MIN(PRICE) AS 가격_최소값
FROM PRODUCT;