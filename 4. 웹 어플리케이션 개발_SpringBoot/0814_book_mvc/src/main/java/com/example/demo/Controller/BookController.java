package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Book;
import com.example.demo.Service.BookService;

// MVC :: Model - View - Controller(+Service)
// 사용자 동작에 따라 어떻게 작업할지 "중재"
@Controller
public class BookController {
	private final BookService bs;
	public BookController(BookService b) {
		this.bs = b;
	}
	
	// (초기 화면) 도서 목록 표현
	@GetMapping("/book/list")
	public ModelAndView BookList(ModelAndView mav) {
		// 1. Service 기능 수행 (DB에서 목록에 표시할 내용 가져오기)
		List<Book> bList = bs.getList();
		
		// 2. ModelAndView 설정 -> 실행
		mav.setViewName("BookList");
		mav.addObject("b", bList);
			// BookList.html 내용을 사용자에게 표시
			// bList(목록에 표현할 DB 내용)를 b 이름으로 전송
		return mav;
	}
	
	// 특정ID의 책 상세 페이지 표현
	@GetMapping("/book/page")
	public ModelAndView BookPage(
			@RequestParam("id") String bId,
			ModelAndView mav) {
		// "?id=[값]"	=> bId 이름으로 값 활용
		
		// 1. Service 기능 수행 (특정ID 책의 전체 칼럼 내용 가져오기)
		List<Book> bData = bs.getData(bId);
		
		// 2. ModelAndView 설정 -> 실행
		mav.setViewName("BookPage");
		mav.addObject("bd", bData);
		return mav;
	}
}





