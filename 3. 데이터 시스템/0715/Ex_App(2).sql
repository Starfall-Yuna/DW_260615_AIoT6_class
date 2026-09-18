-- [기존의 APP 테이블 기반으로 작성]
SELECT * FROM APP;

-- 다운로드수가 100,000 ~ 20,000,000 사이인 데이터의 앱이름, 카테고리 칼럼값 조회
SELECT NAME, CATEGORY, DOWNLOADS FROM APP
    WHERE DOWNLOADS BETWEEN 100000 AND 20000000;

-- 가격이 1000~10000 사이인 데이터의 전체 칼럼 조회 (다운로드수 기준 내림차순 정렬)
SELECT * FROM APP
    WHERE PRICE BETWEEN 1000 AND 10000
    ORDER BY DOWNLOADS DESC;

-- 앱이름이 '카카오톡', '얼불춤'인 데이터의 앱이름과 다운로드수 칼럼값 조회
SELECT NAME, DOWNLOADS FROM APP
    WHERE NAME IN ('카카오톡', '얼불춤');

-- 앱이름이 '톡'으로 끝나는 데이터의 전체 칼럼 조회
SELECT * FROM APP
    WHERE NAME LIKE '%톡';
-- 앱이름이 '집'으로 시작하는 데이터의 전체 칼럼 조회
SELECT * FROM APP
    WHERE NAME LIKE '집%';
