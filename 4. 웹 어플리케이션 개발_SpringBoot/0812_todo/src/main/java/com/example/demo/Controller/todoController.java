package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Todo;
import com.example.demo.Service.todoService;

@Controller
public class todoController {
	private final todoService ts;
	public todoController(todoService t) {
		this.ts = t;
	}
	
	@GetMapping("/")		// localhost:8080
	public String home() {
		return "redirect:/todo";
	}
	@GetMapping("/todo")	// localhost:8080/todo
	public String todoHome() {
		return "todoForm";	// todoForm.html 화면 띄움
	}
	
	@PostMapping("/todo/searchId")
	public ModelAndView searchById(
			@RequestParam("todoId") int targetId,
			ModelAndView mav) {
		// Id를 통해서, 할일 데이터 조회 (Service)
		Todo rs = ts.searchTodoById(targetId);
		
		mav.setViewName("result");
		mav.addObject("id", rs.getId());
		mav.addObject("category", rs.getCategory());
		mav.addObject("content", rs.getContent());
		//mav.addObject("completed", rs.getCompleted());
		if(rs.getCompleted().equals("Y") == true) {	
			// 조회결과의 completed 값이 "Y"일때,
			mav.addObject("completed", "완료");
		}
		else {
			// 조회결과의 completed 값이 "Y"가 아닐 때,
			mav.addObject("completed", "미완료");
		}
		
		return mav;
	}
	
	@PostMapping("/todo/count")
	@ResponseBody
	public String countInComplete() {
		// 전체 데이터 중, 미완료된 데이터 개수 조회 (Service)
		int result = ts.countSQL();
		
		return "미완료된 할일의 개수는 "+result+"개입니다.";
	}
}






