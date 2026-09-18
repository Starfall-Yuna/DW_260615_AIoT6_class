package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

// 해당 프로젝트의 서버가 가동 -> 사용자가 서버 접속 시 링크에 따라서 실행할 내용을 정해줌(중재)
@Controller
public class BasicController {
	@GetMapping("/")	// localhost:8080으로 접속할 때, 아래 함수 실행하라.
	public String home() {
		return "basic/index";	// "Hello World~" 출력
	}
	@GetMapping("/calc")	// localhost:8080/calc으로 접속할 때, 아래 함수 실행하라.
	public String Calc() {	
		return "basic/index_calc";	// "계산기 프로그램입니다" 출력
	}
	
	// name 속성값이 num1인 입력창의 입력값을 n1으로 전달
	// name 속성값이 num2인 입력창의 입력값을 n2로 전달
	// @GetMapping("/execute")	// GET방식  (링크에 내부 정보 노출O)
	@PostMapping("/execute")	// POST방식 (링크에 내부 정보 노출X, 보안 강력)
	@ResponseBody	
	public String executeCalc(
			@RequestParam("num1") int n1,
			@RequestParam("num2") int n2,
			@RequestParam("oper") String ch) {
		// ch의 값에 따라, 연산하는 방식이 나뉘어짐		-> if문 
		int result;
		if(ch.equals("plus") == true) {
			result = n1+n2;
		}
		else if(ch.equals("minus") == true) {
			result = n1-n2;
		}
		else {
			result = n1*n2;
		}
		
		// @ResponseBody 추가X -> return문에 있는 파일을 자동으로 탐색
		// @ResponseBody 추가O -> return문에 있는 문구를 그대로 브라우저 표시
		return "연산결과: "+result;
	}
	// localhost:8080/execute로 실행이 안 되는 이유?
	// 1. 사용자가 링크를 입력해서 접속 방식 -> GET방식 (접속방식 달라서)
	// 2. 3개의 매개변수 값이 전달X
}
