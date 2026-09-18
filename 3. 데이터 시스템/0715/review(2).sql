SELECT * FROM SUBSCRIBE;

-- [칼럼명] BETWEEN [A] AND [B] :: 해당 칼럼의 값이 A~B 사이인 데이터 조회할때 사용
SELECT * FROM SUBSCRIBE
    WHERE PRICE BETWEEN 5000 AND 10000;     -- 5000 이상 10000 이하
SELECT * FROM SUBSCRIBE
    WHERE START_DATE BETWEEN '2025-01-01' AND '2026-12-31';

-- [칼럼명] IN (값1, 값2, ...) :: 해당 칼럼의 값이 () 안에 값 중에 해당되는 데이터 조회할때 사용
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME IN ('유튜브 프리미엄', '제미나이 Plus', '배달의민족 VIP');

INSERT INTO SUBSCRIBE VALUES ('구글 제미나이 무료', 0, NULL);
INSERT INTO SUBSCRIBE VALUES ('제미나이 Pro', 29000, NULL);
INSERT INTO SUBSCRIBE VALUES ('구글 제미나이 Ultra', 119000, NULL);
SELECT * FROM SUBSCRIBE;

-- [칼럼명] LIKE '내용' :: 특정 값이 위치하였거나 포함할 때의 데이터 조회할 때 사용 (%, _)
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME LIKE '%제미나이%';       -- 앱이름 칼럼값에 "제미나이"를 포함하는 데이터 조회
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME LIKE '제미나이%';        -- 앱이름 칼럼값이 "제미나이"로 시작하는 데이터 조회
SELECT * FROM SUBSCRIBE
    WHERE APP_NAME LIKE '%Plus';           -- 앱이름 칼럼값이 "Plus"로 끝나는 데이터 조회