package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Service.BookService;

@Controller	
public class BookController {
	private final BookService bs;
	public BookController(BookService b) {
		this.bs = b;
	}
	
	@GetMapping("/book")		// "localhost:8080/book" 접속할 때
	public String BookHome() {
		return "BookForm";		// BookForm.html 화면 띄움 
	}
	@PostMapping("/rental")
	public ModelAndView doRental(
			@RequestParam("book_id") String bId,
			ModelAndView mav) {
		bs.BookRental(bId);
		
		System.out.println("책 대여가 완료되었습니다.");
		mav.setViewName("BookForm");
		return mav;
	}
	@PostMapping("/return")
	public ModelAndView doReturn(
			@RequestParam("book_id") String bId,
			ModelAndView mav) {
		bs.BookReturn(bId);
		
		System.out.println("책 반납이 완료되었습니다.");
		mav.setViewName("BookForm");
		return mav;
	}
	@PostMapping("/count")
	public ModelAndView doCount(
			ModelAndView mav) {
		Integer result = bs.BookCount();
		
		mav.setViewName("countBook");
		mav.addObject("rs", result);
		return mav;
	}
}



