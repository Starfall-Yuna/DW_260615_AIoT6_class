package com.yse.dev.Book;

import java.util.List;
import java.util.NoSuchElementException;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.yse.dev.Book.DTO.BookCreateDTO;
import com.yse.dev.Book.DTO.BookEditDTO;
import com.yse.dev.Book.DTO.BookListDTO;
import com.yse.dev.Book.DTO.BookReadDTO;
import com.yse.dev.Book.Service.BookService;

@Controller
public class BookController {
	private final BookService bs;
	public BookController(BookService b) {
		this.bs = b;
	}
	
	// (localhost:8080/book/create) 책 생성하기 화면 표현
	@GetMapping("/book/create")	
	public String create() {
		return "book/create";
	}
	
	// @RequestParam("title") String title
	// @RequestParam("price") int price
	//		=> BookCreateDTO bc
	// (create.html "저장"버튼 클릭) 
	//	1. 사용자 입력값 반영하여 BookItem 테이블 insert 수행
	//	2. "/book/read/[책번호]" 이동
	@PostMapping("/book/create")
	public String insertBook(BookCreateDTO bc) {
		Integer target = bs.insert(bc);
		return "redirect:/book/read/"+target;
	}
	
	// (localhost:8080/book/read/[책번호]) 책 상세내용 페이지 화면 표현
	// 	1. Service 통해서, 링크의 책번호에 해당하는 책 데이터 전체 가져오기
	//	2. 1의 내용과 화면 내용(html)을 mav 통하여 실행
	@GetMapping("/book/read/{bookId}")
	public ModelAndView readBook(@PathVariable("bookId") Integer bId) throws NoSuchElementException {
		BookReadDTO result = bs.read(bId);
		
		ModelAndView mav = new ModelAndView();
		mav.setViewName("book/read");
		mav.addObject("rs", result);
		return mav;
	}
	
	// (read.html 삭제 버튼 클릭)
	// 	1. Service 통해서, 지정된 책번호의 책 데이터 삭제
	//	2. "/book/create" 이동
	@GetMapping("/book/delete/{bookId}")
	public String deleteBook(@PathVariable("bookId") Integer bId) throws NoSuchElementException{
		bs.delete(bId);
		
		return "redirect:/book/create";
	}
	
	// (localhost:8080/book/edit/[책번호]) 책 수정 페이지 화면 표시
	//	1. Service 통해서, 기존 책 데이터 조회
	// 	2. 1의 결과와 함께 책 수정 웹페이지 내용 화면 표시
	@GetMapping("/book/edit/{bookId}")
	public ModelAndView edit(@PathVariable("bookId") Integer bId) throws NoSuchElementException {
		BookReadDTO result = bs.read(bId);
		
		ModelAndView mav = new ModelAndView();
		mav.setViewName("book/edit");
		mav.addObject("rs", result);
		return mav;
	}
	
	// (edit.html "수정" 버튼 클릭)
	// 	1. Service 통해서, 지정된 책번호의 책 데이터를 수정
	// 	2. "/book/read" 이동
	@PostMapping("/book/edit/{bookId}")
	public String editBook(BookEditDTO be) {
		bs.edit(be);
		
		return "redirect:/book/read/"+be.getBookId();
	}
	
	// DB에 있는 전체 책에 대한 목록 화면 표시 
	//	1. Service 통해서, 목록에 표현할 책 데이터 가져오기
	//	2. 1의 데이터와 함께, 목록 화면 실행
	@GetMapping("/book/list")
	public ModelAndView showList() {
		ModelAndView mav = new ModelAndView();
		List<BookListDTO> rs = bs.list();
		
		mav.addObject("rs", rs);
		mav.addObject("count", rs.size());
		mav.setViewName("book/list");
		
		return mav;
	}
	
	// 입력한 키워드를 title값으로 포함하는 책 데이터 조회
	//	1. Service 통해서, DB에 대해 검색 수행 + 결과 가져오기
	//	2. 검색결과와 화면 내용(html) 사용자에게 표시
	@PostMapping("/book/search")
	public ModelAndView searchBook(
			@RequestParam("title") String title) {
		List<BookListDTO> result = bs.search(title);
		
		ModelAndView mav = new ModelAndView();
		mav.addObject("rs", result);
		mav.setViewName("book/search");
		return mav;
	}
	
	// 위 내용 수행하다가 DB조회결과 없을 시, 예외(에러) 처리할 내용
	//	=> 에러페이지(html) 화면 띄움 
	@ExceptionHandler(NoSuchElementException.class)
	public ModelAndView noElementFunc(NoSuchElementException ex) {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("error/422");
		mav.setStatus(HttpStatus.UNPROCESSABLE_CONTENT);
		mav.addObject("msg", "책 정보가 없습니다.");
		return mav;
	}
}



