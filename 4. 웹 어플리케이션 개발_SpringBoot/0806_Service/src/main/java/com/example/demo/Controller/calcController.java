package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Service.*;

// Controller :: 사용자 동작에 따라 어떻게 수행할지 "중재"

@Controller
public class calcController {
	// Service의 내용 활용
	//	-> (사전작업) Service 클래스 인스턴스 생성한 이후로 작업해야함
	//	private (각 파일당 하나씩 인스턴스 배정 권장), final(자동 실행되면서 부여된 내용 변동X)
	private final calcService cs;
	public calcController(calcService c) {	// SpringBoot 자동 실행
		this.cs = c;
	}
	
	@GetMapping("/calc")		// localhost:8080/calc 접속할 시,
	public String calcHome() {
		return "calcForm";		// calcForm.html 화면에 띄움
	}
	
	@PostMapping("/doCalc")
	@ResponseBody
	public ModelAndView doCalc(
			@RequestParam("number1") int n1,
			@RequestParam("number2") int n2,
			@RequestParam("oper") String operator,
			ModelAndView mav) {
		// int result = cs.executeAdd(n1, n2);
		
		// Service단에서, 2개의 숫자값과 1개의 연산자를 바탕으로
		// 	각 연산자에 알맞는 연산 결과를 return하는
		//	executeCalc()를 작성하라.
		//		(Controller 파일, Service 파일 변경 필요)
		int result = cs.executeCalc(n1, n2, operator);
		
		// resultForm.html 화면 띄움
		//		(result값을 rs라는 이름으로 전송)
		mav.setViewName("resultForm");
		mav.addObject("rs", result);
		return mav;
	}
}

