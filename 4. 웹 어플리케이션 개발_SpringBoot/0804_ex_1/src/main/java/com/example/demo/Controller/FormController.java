package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class FormController {
	// localhost:8080/input 링크로 접속하면 입력 페이지를 조회
	@GetMapping("/input")
	public String form() {
		return "input";
	}
	// localhost:8080/print로 이동
	@PostMapping("/print")
	public ModelAndView printForm(
			@RequestParam("name") String n, 
			@RequestParam("gender") String g,
			ModelAndView mav) {
		// input.html에서 입력받은
		// 이름의 입력값은 n으로, 성별의 입력값은 g로 불러옴
		
		// 매개변수로 전달받은 name값과 gender값을
		// 출력을 수행하는 html로 "전달"
		
		// print.html 사용자에게 표현
		// (n, g값을 name, gender 이름으로 같이 전송)
		mav.addObject("name", n);
		mav.addObject("gender", g);
		mav.setViewName("print");
		
		return mav;
	}
}
