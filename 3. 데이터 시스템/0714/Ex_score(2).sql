INSERT INTO SCORE VALUES ('Jung', 60, NULL, 70);
INSERT INTO SCORE VALUES ('Han', 90, 75, NULL);

SELECT * FROM SCORE;

-- 알고리즘 점수가 80점 이상이면서 자료구조 점수가 90점 이상인 학생 조회
SELECT * FROM SCORE
    WHERE ALGO>=80 AND DATA>=90;
    
-- 이름이 'Han'이 아닌 학생 조회
SELECT * FROM SCORE
    WHERE NAME <> 'Han';    -- <> (다르다)
SELECT * FROM SCORE
    WHERE NOT NAME='Han';   -- NOT (~아니다)

-- 알고리즘 점수, 자료구조 점수, 네트워크 점수 모두 null값이 아닌 학생 조회
SELECT * FROM SCORE
    WHERE ALGO IS NOT NULL AND
        DATA IS NOT NULL AND
        NETW IS NOT NULL;
-- < 참고 >
--  NOT을 사용해서 동일한 결과 내기
--      (AND <-> OR, IS NULL <-> IS NOT NULL)
SELECT * FROM SCORE
    WHERE NOT (ALGO IS NULL OR
        DATA IS NULL OR
        NETW IS NULL);

-- 3과목의 점수 중 하나라도 90 이상인 학생 조회
SELECT * FROM SCORE
    WHERE ALGO >=90 OR
        DATA >= 90 OR
        NETW >= 90;
-- < 참고 >
SELECT * FROM SCORE
    WHERE NOT (ALGO < 90 AND
        DATA < 90 AND
        NETW < 90);

