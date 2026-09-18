-- 1) BOOK 테이블 생성
--      bname(책제목), author(저자), publisher(출판사), price(가격), pdate(출판일), bstar(별점)
CREATE TABLE BOOK(
    BNAME VARCHAR2(70),
    AUTHOR VARCHAR2(30),
    PUBLISHER VARCHAR2(30),
    PRICE NUMBER,
    PDATE DATE,
    BSTAR NUMBER
);

-- 2) BOOK 테이블에, category(책 카테고리) 칼럼 추가(ADD)
ALTER TABLE BOOK ADD CATEGORY VARCHAR2(30);

SELECT * FROM BOOK;

-- 3) "교보문고" 사이트에 있는 임의의 책 7권의 데이터 기반으로 데이터 삽입(insert) 수행
INSERT INTO BOOK VALUES ('복숭아와 애벌레', '안녕달', '창비', 16800, '2026-07-06', 9.9, '한국그림책');
INSERT INTO BOOK VALUES ('화성에 도시를 세운다면', '잭 와이너스미스', '알에이치코리아', 29800, '2026-06-15', 10, '과학이야기');
INSERT INTO BOOK VALUES ('백지 앞에서', '최은영', '문학동네', 17500, '2026-04-30', 9.7, '한국에세이');
INSERT INTO BOOK VALUES ('우리는 시를 사랑해', '고명재', '문학동네', 15120, '2026-06-19', 10, '한국에세이');
INSERT INTO BOOK VALUES ('연금술사', '파울로 코엘료', '북다', 16800, '2026-07-03', 10, '중남미소설');

-- 4) 모든 책 데이터에 대하여, 가격 데이터를 10% 할인가로 변경
UPDATE BOOK SET PRICE=PRICE-(PRICE*0.1);
-- UPDATE BOOK SET PRICE=PRICE*0.9;

-- 5) 테이블 삭제 :: TRUNCATE/DELETE -> DROP
TRUNCATE TABLE BOOK;
DROP TABLE BOOK;
