-- 구독 서비스 테이블 생성(3개의 칼럼)
CREATE TABLE SUBSCRIBE(
    APP_NAME VARCHAR2(100),
    PRICE NUMBER,
    START_DATE DATE
);

INSERT INTO SUBSCRIBE VALUES ('유튜브 프리미엄', 14900, '2025-09-01');
INSERT INTO SUBSCRIBE VALUES ('카카오톡 톡서랍', 2200, '2023-01-01');
INSERT INTO SUBSCRIBE VALUES ('챗GPT 5.5', 29000, '2023-07-15');
INSERT INTO SUBSCRIBE VALUES ('요기요 요기패스', 9500, '2026-06-30');

SELECT * FROM SUBSCRIBE;

-- 집계 함수 :: COUNT(), MIN(), MAX(), SUM(), AVG()
SELECT COUNT(*) FROM SUBSCRIBE;

SELECT 
    MAX(PRICE) AS 가격_최대,
    MIN(PRICE) AS 가격_최소,
    SUM(PRICE) AS 가격_합,
    AVG(PRICE) AS 가격_평균
FROM SUBSCRIBE;

-- WHERE절 :: 조건에 맞는 데이터만 필터링
--  - [비교 연산] =(같다), <>(다르다), 부등호   (NULL값은 비교대상X)
SELECT * FROM SUBSCRIBE
    WHERE START_DATE >= '2025-01-01';   -- 구독 시작일이 2025/01/01 이후인 데이터만 조회
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME = '카카오톡 톡서랍';   -- 구독앱 이름이 '카카오톡 톡서랍'인 데이터만 조회
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME <> '카카오톡 톡서랍';  -- 구독앱 이름이 '카카오톡 톡서랍'이 아닌 데이터만 조회

--  - [NULL 검색] IS NULL, IS NOT NULL
INSERT INTO SUBSCRIBE VALUES ('제미나이 Plus', 7500, NULL);
INSERT INTO SUBSCRIBE VALUES (NULL, 10000, '2020-05-30');
SELECT * FROM SUBSCRIBE;

-- 구독 시작일이 NULL인 데이터 전체 칼럼 조회
SELECT * FROM SUBSCRIBE
    WHERE START_DATE IS NULL;
-- 구독앱 이름이 NULL이 아닌 데이터 전체 칼럼 조회
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME IS NOT NULL;

-- [논리연산] AND, OR, NOT
SELECT * FROM SUBSCRIBE
    WHERE PRICE <10000 AND START_DATE >= '2026-01-01';
        -- 가격이 10000원 미만이고(AND), 구독 시작일이 '2026-01-01' 이후인 데이터만 조회
SELECT * FROM SUBSCRIBE
    WHERE PRICE <10000 OR START_DATE >= '2026-01-01';
        -- 가격이 10000원 미만이거나(OR) 구독 시작일이 '2026-01-01' 이후인 데이터만 조회
SELECT * FROM SUBSCRIBE
    WHERE NOT APP_NAME = '요기요 요기패스';
        -- 구독앱 이름이 '요기요 요기패스'이 아닌 데이터만 조회


