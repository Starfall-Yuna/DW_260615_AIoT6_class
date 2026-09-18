CREATE TABLE APP(
    NAME VARCHAR2(50),
    CATEGORY VARCHAR2(30),
    PRICE NUMBER,
    DOWNLOADS NUMBER
);

INSERT INTO APP VALUES ('카카오톡', '소셜', 0, 50000000);
INSERT INTO APP VALUES ('BlueSky', '소셜', 0, 90000);
INSERT INTO APP VALUES ('얼불춤', '게임', 2200, 1500000);
INSERT INTO APP VALUES ('꿈의집', '게임', 0, 3500000);
INSERT INTO APP VALUES ('위버스', '소셜', 0, 10000);
SELECT * FROM APP;

-- 무료앱 데이터만 조회하여, 전체 칼럼 조회
SELECT * FROM APP
    WHERE PRICE = 0;    -- 앱 가격이 0(무료앱)인 데이터만 조회

-- 카테고리가 '소셜'이고 다운로드 수가 100,000 이상인 데이터만 조회하여, 앱 이름 칼럼 조회
SELECT NAME FROM APP
    WHERE CATEGORY = '소셜' AND DOWNLOADS >= 100000;
    
-- 카테고리가 '게임'이고 가격이 1,000 이상인 데이터만 조회하여, NAME 기준 오름차순 정렬
INSERT INTO APP VALUES ('마인크래프트', '게임', 9900, 5000000);
SELECT * FROM APP
    WHERE CATEGORY='게임' AND PRICE >=1000
    ORDER BY NAME ASC;
