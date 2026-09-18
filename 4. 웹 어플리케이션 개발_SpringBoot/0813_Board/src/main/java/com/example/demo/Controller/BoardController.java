package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Board;
import com.example.demo.Service.BoardService;

@Controller
public class BoardController {
	private final BoardService bs;
	public BoardController(BoardService b) {
		this.bs = b;
	}
	
	@GetMapping("/")		// localhost:8080 접속할 때
	public String redirect() {
		return "redirect:/board/list";	// localhost:8080/board/list 이동
	}
	// 게시판 목록 표현 (초기 화면)
	@GetMapping("/board/list")	// localhost:8080/board/list 접속할 때
	public ModelAndView ShowList(ModelAndView mav) {
		// 1. 목록에 표시할 내용 가져오기 (Service)
		List<Board> listdata = bs.getAll();
		
		// 2. ModelAndView 설정
		mav.setViewName("BoardList");
		mav.addObject("rst", listdata);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
	
	// 게시판 상세페이지 (id값에 따라 불러오는 게시판 내용이 다름)
	@GetMapping("/board/detail")
	public ModelAndView showDetail(
			@RequestParam("id") int boardId,
			ModelAndView mav) {
		// 1. 특정ID값인 게시판의 모든 내용 조회 (Service)
		List<Board> result = bs.getContent(boardId);
		
		// 2. ModelAndView 설정
		mav.setViewName("BoardContent");
		mav.addObject("res", result);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
}




