package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Service.LoginService;

@Controller
public class LoginController {
	private final LoginService ls;
	public LoginController(LoginService l) {
		this.ls = l;
	}
	
	@GetMapping("/")
	@ResponseBody
	public String testHome() {
		return "서버 정상 가동";
	}
	
	@GetMapping("/login")	// localhost:8080/login 접속할 시 
	public String loginHome() {
		return "loginForm";	// loginForm.html 화면 띄움
	}
	@PostMapping("/doLogin")
	public ModelAndView executeLogin(
			@RequestParam("id") String input_id,
			@RequestParam("pw") String input_pw, 
			ModelAndView mav) {
		// isLogin :: 로그인 성공/실패 여부 구하여 저장
		boolean isLogin = ls.checkLogin(input_id, input_pw);
		
		if(isLogin == true) {
			System.out.println("로그인 성공");
			
			mav.setViewName("success_login");
			mav.addObject("id", input_id);
			return mav;
		}
		else {
			System.out.println("로그인 실패");
			
			mav.setViewName("fail_login");
			return mav;
		}
	}
	
	@GetMapping("/signIn")		// localhost:8080/signIn 접속할 시
	public String signInForm() {
		return "signIn";		// signIn.html 화면 띄움
	}
	@PostMapping("/doSignIn")
	public ModelAndView executeSignIn(
			@RequestParam("id") String input_id,
			@RequestParam("pw") String input_pw,
			@RequestParam("name") String input_n,
			ModelAndView mav) {
		ls.joinMember(input_id, input_pw, input_n);
		
		mav.setViewName("loginForm");
		return mav;
	}
}




