-- * WEATHER 테이블 생성
CREATE TABLE WEATHER(
    DATA_ID VARCHAR2(10) PRIMARY KEY,       -- [기상관측 데이터 번호] VARCHAR2, 식별자(기본키)
    REGION VARCHAR2(30) UNIQUE,             -- [지역명] VARCHAR2, 중복 입력X
    SKY VARCHAR2(30) NOT NULL CHECK (SKY IN ('맑음', '흐림', '비', '눈')),
            -- [하늘 상태] VARCHAR2, NULL 입력X, '맑음', '흐림', '비', '눈' 중 하나만 입력O
    TEMP NUMBER CHECK (-50 <= TEMP AND TEMP <= 60),     -- [온도] NUMBER, -50 이상 60 이하만 입력O
    HUMIDITY NUMBER CHECK (HUMIDITY BETWEEN 0 AND 100),  -- [습도] NUMBER, 0 이상 100 이하만 입력O
    DATA_DATE DATE NOT NULL                 -- [관측일시] DATE, NULL 입력X
);
DROP TABLE WEATHER;

-- * 위의 WEATHER에 총 10개 데이터 삽입하기
INSERT INTO WEATHER VALUES ('1', '서울', '비', 29, 70, '2026-07-13');
INSERT INTO WEATHER VALUES ('2', '대구', '맑음', 35, 60, '2026-07-15');
INSERT INTO WEATHER VALUES ('3', '대전', '흐림', 30, 50, '2026-07-14');
INSERT INTO WEATHER VALUES ('4', '부산', '흐림', 31, 30, '2026-07-12');
INSERT INTO WEATHER VALUES ('5', '제주', '비', 33, 65, '2026-07-10');

SELECT * FROM WEATHER;


