package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class BookService {
	private final JdbcTemplate jt;
	public BookService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// 책id를 기준으로 책 선택 후 "대여" (대여 불가능한 상태에 대한 예외 처리 진행)
	public void BookRental(String bookId) {
		String sql = """
				update book set rental = 'N'
				where book_id = ? AND rental = 'Y';
				""";
		Integer count = jt.update(sql, bookId);	
			// count (sql문에 의해 영향받은 데이터 개수 저장)
		
		if(count == 0) {
			throw new IllegalStateException("대여할 수 없는 도서입니다.");
		}
	}
	// 책id를 기준으로 책 선택 후 반납 (반납 불가능한 상태에 대한 예외 처리 진행)
	public void BookReturn(String bookId) {
		String sql = """
				update book set rental = 'Y'
				where book_id = ? and rental = 'N';
				""";
		Integer count = jt.update(sql, bookId);
			// count (sql문에 의해 영향받은 데이터 개수 저장)
		if(count == 0) {
			throw new IllegalStateException("반납할 수 없는 도서입니다.");
		}
	}
	// "대여 가능한" 책 권수 조회 기능
	public Integer BookCount() {
		String sql = """
				select count(*) from book
				where rental = 'Y'
				""";
		// rental = 'Y'인 데이터 개수 조회
		
		Integer count = jt.queryForObject(sql, Integer.class);
		return count;
	}
}






