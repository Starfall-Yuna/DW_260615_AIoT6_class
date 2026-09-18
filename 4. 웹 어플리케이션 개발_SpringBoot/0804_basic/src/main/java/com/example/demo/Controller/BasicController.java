package com.example.demo.Controller;

// 프레임워크 :: 특정 목적(웹, 앱, ...)에 맞추어, 보다 편리하게 개발하기 위한 도구 상자
// 	SpringBoot :: 웹개발 목적 Java 기반 프레임워크
// 의존성(Dependency) :: 라이브러리(Library), 여러 명령어들을 체계적으로 갖춘 것
// 	어노테이션(@) :: 의존성의 기능들 중 하나

// Ctrl + Shift + o (Dependency의 어노테이션 자동 import)
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

// WhiteLabel Error Page :: 서버 가동 ok, 지정된 링크에 띄울 html 페이지를 못 찾음

@Controller
public class BasicController {
	// 0. 서버 테스트
	@GetMapping("/")		// localhost:8080 접속할 때
	@ResponseBody	// 주어진 return값을 그대로 브라우저에 띄움
	public String testHome() {
		return "테스트 페이지입니다.";
	}
	
	// 1. 덧셈 연산 수행하는 계산기 프로그램
	@GetMapping("/calc")	// localhost:8080/calc 접속할 때
	public String calcHome() {
		return "calcForm";
	}
	@PostMapping("/calc")
	@ResponseBody
	public String executeCalc(
			@RequestParam("number1") int n1,
			@RequestParam("number2") int n2) {
		// number1 태그의 입력값을 여기에서는 n1 이름으로 활용
		// number2 태그의 입력값을 여기에서는 n2 이름으로 활용
		int result = n1+n2;
		return "연산결과: "+result;
	}
	
	// 2. 사칙연산 수행하는 계산기 프로그램
	@GetMapping("/pro")		// localhost:8080/pro 접속할 시
	public String proCalcHome() {
		return "proCalcForm";
	}
	// get방식 :: 서버로 전달된 값이 링크 노출O
	// post방식 :: 서버로 전달된 값이 링크 노출X (보안 강력)
	@PostMapping("/execute")	
	@ResponseBody
	public ModelAndView executeProCalc(
			@RequestParam("number1") int n1, 
			@RequestParam("number2") int n2,
			@RequestParam("operator") String op,
			ModelAndView mav) {
		// 2개의 숫자 입력값, 1개의 선택된 연산자
		// ModelAndView :: 서버에서 전달된 값을 특정 디자인의 브라우저에 띄울 때 사용
		
		int result;
		// 몫 나누기, 나머지 나누기 수행될 수 있도록 코드 추가
		if(op.equals("plus") == true) { result = n1+n2; }
		else if(op.equals("minus") == true) { result = n1-n2; }
		else if(op.equals("multi") == true) { result = n1*n2; }
		else if(op.equals("division") == true) { 
			// "나눗셈을 수행할 때, n2가 0이면 안된다."
			if(n2 == 0) {
				// IllegalArgumentException :: 부적절한 매개변수에 대한 예외(오류)
				throw new IllegalArgumentException("0으로 나눌 수 없습니다.");
				// 실행 중단
			}
			result = n1/n2;
		}
		else { result = n1%n2; }
		
		mav.addObject("rs", result);
		mav.setViewName("ResultForm");
		// ResultForm.html로 이동 (result값을 rs라는 이름으로 같이 전송)
		
		return mav;
	}
}






