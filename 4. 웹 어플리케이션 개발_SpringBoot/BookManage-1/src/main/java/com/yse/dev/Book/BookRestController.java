package com.yse.dev.Book;

import java.util.NoSuchElementException;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.yse.dev.Book.DTO.BookReadDTO;
import com.yse.dev.Book.Service.BookService;

// API ::
//	1. 사용자가 네이버에 "대전 날씨" 검색
//	2. 네이버 프로그램 :: 기상청 데이터, 웨더아이 데이터(오픈API) 불러오기 시도
//	3. 네이버 프로그램 :: [불러오기 성공할 시] 검색창 표현
//		=> 타인의 DB나 데이터 접근에 활용
//	=> REST API :: 대표적인 웹 API (대중적으로 데이터 교환에 활용하는 규칙)

@RestController
public class BookRestController {
	private final BookService bs;
	public BookRestController(BookService b) {
		this.bs = b;
	}
	
	// 책번호에 대한 책 데이터 검색 수행 -> 검색결과를 rest api 전달
	// "localhost:8080/api/book/5" 요청 ->
	//		5번 책 데이터 전체(Entity)로 응답(Response)
	@GetMapping("/api/book/{bookId}")
	public ResponseEntity<BookReadDTO> searchBook(@PathVariable("bookId") Integer bId) {
		try {
			BookReadDTO brd = bs.read(bId);
			
			// ok() :: 정상적으로 처리됨을 알림 (200 처리)
			return ResponseEntity.ok(brd);
		}catch(NoSuchElementException ex) {
			// NOT_FOUND :: 데이터를 찾지 못해 비정상적으로 처리됨 (404 처리)
			return ResponseEntity
					.status(HttpStatus.NOT_FOUND)
					.build();
		}
	}
}




