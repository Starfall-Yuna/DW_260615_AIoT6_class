package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Todo;
import com.example.demo.Service.TodoService;

@Controller
public class TodoController {
	private final TodoService ts;
	public TodoController(TodoService t) {
		this.ts = t;
	}
	
	@GetMapping("/")			// localhost:8080 접속할 때
	public String start() {
		return "redirect:/todo";	// localhost:8080/todo 이동
	}
	@GetMapping("/todo")		// localhost:8080/todo 접속할 때
	public String todoStart() {
		return "StartHome";		// startHome.html 화면 띄움
	}
	
	@PostMapping("/todo/show")
	public ModelAndView showEntire(ModelAndView mav) {
		// 1. todo 전체 데이터 조회 (Service)
		List<Todo> result = ts.selectSQL1();
		
		// 2. ModelAndView 설정
		mav.setViewName("showAll");
		mav.addObject("alldata", result);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
	
	@PostMapping("/todo/category")
	public ModelAndView Filtering(
			@RequestParam("category") String cg,
			ModelAndView mav) {
		// 1. 선택한 카테고리 데이터 조회 (Service)
		List<Todo> result = ts.FilterTodo(cg);
		
		// 2. ModelAndView 설정
		mav.setViewName("showAll");
		mav.addObject("alldata", result);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
}





