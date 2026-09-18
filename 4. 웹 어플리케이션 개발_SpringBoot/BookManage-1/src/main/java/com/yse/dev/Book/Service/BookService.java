package com.yse.dev.Book.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

import org.springframework.stereotype.Service;

import com.yse.dev.Book.DTO.BookCreateDTO;
import com.yse.dev.Book.DTO.BookEditDTO;
import com.yse.dev.Book.DTO.BookListDTO;
import com.yse.dev.Book.DTO.BookReadDTO;
import com.yse.dev.Book.Entity.BookItem;
import com.yse.dev.Book.Entity.BookItemRepository;

@Service
public class BookService {
	// DB연산하려면? Entity, Repository 필요
	private final BookItemRepository br;
	public BookService(BookItemRepository b) {
		this.br = b;
	}
	
	// 사용자 입력값 반영하여 BookItem 테이블 insert 수행
	//	1. DB insert를 통해, 삽입할 데이터 구성 (Entity 활용)
	//	2. 1을 기반으로, insert 실행
	//	3. 상세페이지 이동에 필요한 bookId값 결과로 제시
	public Integer insert(BookCreateDTO bc) {
		BookItem b = BookItem.builder()
				.title(bc.getTitle())
				.price(bc.getPrice())
				.build();
		
		br.save(b);
		
		return b.getBookId();
	}
	
	// 특정 책번호(bId)에 해당하는 책 데이터 전체 가져오기 
	//	1. DB내용 가져오기 위해, (엔티티 형식에 맞춰) 책 데이터 검색+가져오기
	//	2. 웹에 표현하기 위해, (DTO 형식에 맞춰) 책 데이터 구성+Controller 넘겨주기
	public BookReadDTO read(Integer bId) throws NoSuchElementException {
		// findById() :: PK칼럼 기준 데이터 검색
		BookItem b = br.findById(bId).orElseThrow();
		
		BookReadDTO brd = new BookReadDTO();
		brd.setBookId(b.getBookId());	// 검색결과 책번호 -> DTO 책번호 설정
		brd.setTitle(b.getTitle());
		brd.setPrice(b.getPrice());
		brd.setInsertDateTime(b.getInsertDateTime());
		return brd;
	}
	
	// 특정 책번호의 책 데이터 삭제
	//	1. 삭제할 책 데이터 검색
	//	2. 1의 데이터 삭제
	public void delete(Integer bId) throws NoSuchElementException {
		BookItem b = br.findById(bId).orElseThrow();
		
		br.delete(b);
	}
	
	// 특정 책번호의 책 데이터 수정
	//	1. 수정할 책 데이터 검색
	//	2. 기존 데이터 일부 값 변경 + DB 반영
	public void edit(BookEditDTO be) {
		BookItem b = br.findById(be.getBookId()).orElseThrow();
		
		b.setTitle(be.getTitle());
		b.setPrice(be.getPrice());
		br.save(b);
	}
	
	// DB의 책 데이터 전체 불러오기
	// 	1. DB내용 가져오기 위해, (엔티티 형식에 맞춰) 책 데이터 "전체 가져오기"
	//	2. 웹에 표현하기 위해, (DTO 형식에 맞춰) 각 책 데이터 구성+Controller 넘겨주기
	public List<BookListDTO> list() {
		List<BookItem> bList = br.findAll();
		
		// [책번호, 책이름] 쌍의 데이터를 여러개 저장할 수 있는 공간만 만들어줌
		List<BookListDTO> result = new ArrayList<>();
		for(BookItem b: bList) {
			// b라는 이름을 통해서, bList의 데이터 하나하나 접근
			
			BookListDTO bd = new BookListDTO();
			bd.setBookId(b.getBookId());
			bd.setTitle(b.getTitle());
			result.add(bd);	// 리스트에 값 추가
		}
		return result;
		
	}
	// 특정 키워드(target)를 title값으로 포함하는 책 데이터 조회
	//	1. DB 검색 수행+검색결과 가져오기
	//	2. Entity -> DTO 변환 결과 전달
	public List<BookListDTO> search(String target) {
		List<BookItem> sr = br.findByTitleContaining(target);
		
		List<BookListDTO> result = new ArrayList<>();
		for(BookItem b: sr) {
			BookListDTO bd = new BookListDTO();
			bd.setBookId(b.getBookId());
			bd.setTitle(b.getTitle());
			result.add(bd);
		}
		return result;
	}
//	List<BookListDTO> result
//	 ├─ BookListDTO
//	 │   ├─ bookId = 1
//	 │   └─ title = "Java의 정석"
//	 │
//	 ├─ BookListDTO
//	 │   ├─ bookId = 2
//	 │   └─ title = "Python 기초"
//	 │
//	 └─ BookListDTO
//	     ├─ bookId = 3
//	     └─ title = "html, css의 정석"
}






