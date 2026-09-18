package com.example.demo.Service;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Book;

// "기능 정의"
@Service
public class BookService {
	private final JdbcTemplate jt;
	public BookService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// DB에서 목록에 표시할 내용 가져오기
	// (필요한 내용 :: X / 결과값 :: 목록에 표현할 모든 DB 데이터)
	//		-> DB에서 실행할 sql문 미리 구상
	public List<Book> getList(){
		String sql = """
				select book_id, name
				from book
				""";
		List<Book> result = jt.query(
			sql,
			// select 결과를 rs 이름으로 확인
			// 	조회 결과를 Java에서 사용O 가공 (Book 생성자)
			(rs, ignored) -> new Book(
				rs.getString("book_id"),
				rs.getString("name"),
				0
			)
		);
		return result;
	}
	
	// 특정ID 책의 전체 칼럼 내용 가져오기
	// (필요한 값 :: 특정ID / 결과값 :: 검색한 책 데이터 )
	//		"select * from book where book_id = [특정값]"
	public List<Book> getData(String targetId){
		String sql = """
				select * from book
				where book_id = ?
				""";
		List<Book> result = jt.query(
			sql,
			// rs라는 이름으로 select 결과를 확인
			(rs, ignored) -> new Book(
				rs.getString("book_id"),
				rs.getString("name"),
				rs.getInt("price")
			),
			targetId
		);
		return result;
	}
}






