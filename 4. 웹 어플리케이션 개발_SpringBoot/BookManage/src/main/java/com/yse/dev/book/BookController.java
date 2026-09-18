package com.yse.dev.book;

import java.util.NoSuchElementException;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.yse.dev.book.Service.BookService;
import com.yse.dev.book.dto.BookCreateDTO;
import com.yse.dev.book.dto.BookEditDTO;
import com.yse.dev.book.dto.BookReadDTO;

// - Controller :: 사용자의 동작에 따라 어떤 작업을 할지 "중재/통제"

@Controller
public class BookController {
	private final BookService bs;
	public BookController(BookService b) {
		this.bs = b;
	}
	
	// 책 데이터 생성에 필요한 값 입력받는 화면 띄움
	@GetMapping("/book/create")		// localhost:8080/book/create
	public String create() {
		return "book/create";		// book폴더 안의 create.html 화면 띄움
	}
	
//	@RequestParam("title") String title,
//	@RequestParam("price") int price
	@PostMapping("/book/create")
	public String insertBook(BookCreateDTO bc) {
		// bc.title = "html, css 정석"
		// bc.price = 17000
		
		// 1. Service 통해서, insert문 수행
		// 	방금 생성한 책 데이터의 책번호 target 저장
		Integer target = bs.insert(bc);
		// 2. 방금 생성한 책 데이터 상세페이지 이동
		return "redirect:/book/read/"+target;
		// (ex) localhost:8080/book/read/10
	}
	
	@GetMapping("/book/read/{id}")
	@ResponseBody
	public ModelAndView readBook(@PathVariable("id") Integer bId) throws NoSuchElementException{
		// 링크에 있는 {id} 위치의 값을 bId 이름으로 불러옴
		
		// 1. ModelAndView 작성 준비
		ModelAndView mav = new ModelAndView();
		
		// 2. Service 통해서, bId를 책번호로 갖는 책 전체 데이터 가져오기
		BookReadDTO result = bs.read(bId);
		
		// 3. ModelAndView 설정+실행
		mav.setViewName("book/read");
		mav.addObject("rs", result);
		
		return mav;
	}
	
	@GetMapping("/book/edit/{id}")
	public ModelAndView edit(@PathVariable("id") Integer bId) throws NoSuchElementException{
		// 링크에 있는 {id} 값을 bId 이름으로 활용
		
		ModelAndView mav = new ModelAndView();
		
		// 1. 사용자에게 보여줄 기존 데이터 조회
		BookReadDTO result = bs.read(bId);
		// 2. 조회결과+웹페이지 내용 mav 설정
		mav.addObject("rs", result);
		mav.setViewName("book/edit");
		
		return mav;
	}
	
//	@PathVariable("id") Integer bId,
//	@RequestParam("title") String title,
//	@RequestParam("price") int price
	// => (DTO :: 기존 데이터의 책번호, 가격, 제목)
	@PostMapping("/book/edit/{bookId}")
	public String editBook(BookEditDTO be) {
		// 1. service 통해서, bId번호의 책 데이터 값 수정
		bs.edit(be);
		
		return "redirect:/book/read/"+be.getBookId();
	}
	
	@GetMapping("/book/delete/{bookId}")
	public String deleteBook(@PathVariable("bookId") Integer bId) {
		// 1. Service 통해서, bId 책번호로 가지는 책 데이터 삭제
		bs.delete(bId);
		// 2. /book/create로 이동
		return "redirect:/book/create";
	}
	
	// DB데이터 조회 실패할 때, 실행하던 것을 멈추고 아래 내용을 구동 (throws 명시된 항목에 대해서만)
	@ExceptionHandler(NoSuchElementException.class)
	public ModelAndView noSuchElementFunc(NoSuchElementException ex) {
		System.out.println("에러 발생");
		ModelAndView mav = new ModelAndView();
		mav.setStatus(HttpStatus.UNPROCESSABLE_CONTENT);
		mav.addObject("msg", "책 정보가 없습니다.");	
		mav.setViewName("error/422");
		return mav;
	}
}







