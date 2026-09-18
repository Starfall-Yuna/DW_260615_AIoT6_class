package com.example.demo.Controller;

// 프레임워크 :: 특정 목적(웹, 앱, 게임, ...)에 맞추어, 편리하게 개발하기 위한 도구 상자 
// 의존성(Dependency) :: 라이브러리(Library), 여러 명령어들을 체계적으로 갖춘 것
// 		- 어노테이션(@) :: 의존성 중 하나

// (예시) org폴더 >> springframework폴더 >> stereotype클래스 >> Controller어노테이션
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

// Boot Dashboard 실행 -> 프로젝트가 있는 서버 가동

@Controller
public class ScoreController {
	@GetMapping("/")	// "localhost:8080/" 접속할 때, 아래의 testHome() 실행
	@ResponseBody		// return문을 웹페이지에 그대로 표시
	public String testHome() {
		return "테스트 페이지입니다";
	}
	@GetMapping("/test")	// "localhost:8080/test" 접속할 때, 아래의 webTest() 실행
	public String webTest() {
		return "test";		// test 이름의 파일로 이동
	}
	
	@GetMapping("/login")	// "localhost:8080/login" 접속할 때, 아래의 showLogin() 실행
	public String showLogin() {
		return "loginForm";
	}
	@PostMapping("/doLogin")
	public ModelAndView executeLogin(
			@RequestParam("id") String input_id,
			@RequestParam("pw") String input_pw,
			ModelAndView mav) {
		// html의 name="id"인 태그 입력값을 input_id 이름으로 불러옴
		// html의 name="pw"인 태그 입력값을 input_pw 이름으로 불러옴
		
		// ModelAndView :: "View", 사용자에게 표시할 화면 구성
		if(input_id.equals("admin") == true && input_pw.equals("0000") == true) {
			System.out.println("로그인 성공");
			
			mav.setViewName("success_login");	// success_login.html 표현
			mav.addObject("id", input_id);		// input_id값을 id라는 이름으로 html로 데이터 전송
			return mav;
		}
		else {
			System.out.println("로그인 실패");
			
			mav.setViewName("fail_login");	
			mav.addObject("id", input_id);
			mav.addObject("pw", input_pw);
			return mav;
		}
	}
}



