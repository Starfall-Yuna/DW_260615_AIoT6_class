package com.yse.dev.book.Service;

import java.util.NoSuchElementException;

import org.springframework.stereotype.Service;

import com.yse.dev.book.Entity.Book;
import com.yse.dev.book.Entity.BookRepository;
import com.yse.dev.book.dto.BookCreateDTO;
import com.yse.dev.book.dto.BookEditDTO;
import com.yse.dev.book.dto.BookReadDTO;

@Service
public class BookService {
	private final BookRepository br;
	public BookService(BookRepository b) {
		this.br = b;
	}
	
	// Book 테이블에 insert문 수행하는 기능
	public Integer insert(BookCreateDTO bc) {
		// (String name, int price)
		
		// 1. Entity 기준 테이블 삽입할 데이터 구성
		// @Builder 통해서 생성된 함수 builder()
		Book b = Book.builder()	
				.title(bc.getTitle())
				.price(bc.getPrice())
				.build();
			// 전달된 내용(DTO) 중 책제목, 책가격 값을 불러와서 삽입
		// 2. insert문 수행	-> Repository 활용
		br.save(b);
		// 3. insert를 수행한 책의 책번호 값을 return
		return b.getBookId();
	}
	
	// 특정 책번호를 갖는 책 전체 데이터 가져오기
	// (사전에 필요한 값 :: 책번호(Integer) /
	//		결과값 :: 검색된 책의 전체 칼럼 데이터)
	public BookReadDTO read(Integer id) throws NoSuchElementException {
		// 1. Entity 기준 id값 기반으로, 책 데이터 검색(select)
		// 		PK인 bookId 칼럼 기준 검색 (조회 실패 -> 에러 발생)
		Book search = br.findById(id).orElseThrow();
//		System.out.println(search.getBookId());
//		System.out.println(search.getTitle());
		// 검색한 책의 책번호+책이름+책가격+데이터 생성시점 (4가지)
		
		// 2. 검색결과 가공 후 return
		BookReadDTO brd = new BookReadDTO();
		brd.fromBook(search);	// search의 DB내용을 brd로 옮겨줌
		return brd;
	}
	
	// 특정 번호의 책 데이터 값 수정
	// (DTO :: 기존 데이터의 책번호, 가격, 제목)
	public void edit(BookEditDTO be){
		// 1. bookId 번호인 책 데이터 기존값 불러오기
		Book b = br.findById(be.getBookId()).orElseThrow();
		
		// 2. 1의 데이터에 대해 수정 진행
		// 	사용자의 입력값(get())을 새로 반영할 값(b)에 저장(set())
		b.setTitle(be.getTitle());
		b.setPrice(be.getPrice());
		
		// 3. DB 값 갱신
		br.save(b);
	}
	
	// 특정 책번호를 가지는 책 데이터 삭제
	public void delete(Integer bId) {
		// - 삭제하고자 하는 책 검색
		Book b = br.findById(bId).orElseThrow();
		// - 검색된 책 데이터 삭제
		br.delete(b);
	}
}








