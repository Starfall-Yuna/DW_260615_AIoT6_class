-- 프로시저 :: SQL 상의 함수

-- PRINT_HELLO 프로시저 생성
--CREATE OR REPLACE PROCEDURE [프로시저_이름](
--매개변수 구성
--)
--IS
--  임의의 필요한 변수 생성
--BEGIN
--  수행할 명령어
--END;/

CREATE OR REPLACE PROCEDURE PRINT_HELLO
IS
BEGIN
    -- 프로시저 내용
    DBMS_OUTPUT.PUT_LINE('HELLO WORLD!');
END;
/

-- PRINT_HELLO 프로시저 실행(EXEC)
--  1) 보기 >> DBMS 출력 탭 클릭
--  2) 사용하고 있는 서버로 연결
--  3) DBMS_OUTPUT.PUT_LINE 함수 실행
EXEC PRINT_HELLO;


CREATE OR REPLACE PROCEDURE PRINT_SUM(
    NUM1 IN NUMBER,
    NUM2 IN NUMBER
)
IS
    RESULT NUMBER;
BEGIN
    -- [SQL] = "같다"
    RESULT := NUM1 + NUM2;  -- NUM1과 NUM2를 더한 값을 RESULT에 저장
    DBMS_OUTPUT.PUT_LINE(RESULT);
END;
/

EXEC PRINT_SUM(30,10);

