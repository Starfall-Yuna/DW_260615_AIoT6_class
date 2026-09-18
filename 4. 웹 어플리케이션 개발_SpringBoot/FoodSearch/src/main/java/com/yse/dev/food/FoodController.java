package com.yse.dev.food;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.yse.dev.food.DTO.AdminAccessDTO;
import com.yse.dev.food.Service.AdminService;

@Controller
public class FoodController {
	private final AdminService as;
	public FoodController(AdminService a) {
		this.as = a;
	}
	
	@GetMapping("/")		// localhost:8080 접속 -> localhost:8080/food 자동 접속
	public String home() {
		return "redirect:/food";
	}
	@GetMapping("/food")	// localhost:8080/food 접속하면, login.html 화면 띄움
	public String foodHome() {
		return "login";
	}
	
	// AdminAccessDTO ("관리자 계정 데이터에 접근하기 위한 DTO")
//	@RequestParam("id") String id,
//	@RequestParam("pw") String pw		=> AdminAccessDTO
	@PostMapping("/show")
	public String doLogin(AdminAccessDTO aa) {
		// 사용자가 입력한 아이디값(id), 비밀번호값(pw)
		
		// 1. Service 통해서, 입력받은 id/pw가 테이블에 있는 내용인지 확인
		Boolean rs = as.isLogin(aa);
		// 2. 1의 결과에 따라 아래처럼 동작하게끔 설정
		//		- 로그인 성공하였을때, foodList.html 화면 띄움
		//		- 로그인 실패하였을때, error.html("에러발생") 화면 띄움
		if(rs == true) {
			return "foodList";
		}
		else {
			return "error";
		}
	
		// 로그인이 필요한 기능 :: session, cookie 사용
	}
}


