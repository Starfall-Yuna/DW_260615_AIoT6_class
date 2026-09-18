package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Member;
import com.example.demo.Service.MemberService;

@Controller
public class MemberController {
	private final MemberService ms;
	public MemberController(MemberService m) {
		this.ms = m;
	}
	// ms를 통해, Service의 기능 활용
	
	@GetMapping("/")		// localhost:8080
	public String home() {
		// return "memberForm";
		return "redirect:/member";	// /member 이동
	}
	@GetMapping("/member")	// localhost:8080/member
	public String memberHome() {
		return "memberForm";
	}
	
	@PostMapping("/member/count")
	public ModelAndView showCount(ModelAndView mav) {
		// DB에 저장된 Member 데이터 총 개수 조회 (Service)
		int count = ms.countSQL();
		// count :: countSQL() 실행한 후 return값 저장
		
		mav.setViewName("ViewCount");
		mav.addObject("result", count);
		// ViewCount.html 화면 띄움 (count값 result이름 전송)
		
		return mav;
	}
	
	@PostMapping("/member/search")
	public ModelAndView searchMember(
			@RequestParam("targetId") String target,
			ModelAndView mav) {
		// 특정 ID를 가진 사용자 정보 조회 (Service)
		Member result = ms.searchSQL(target);
		
		mav.setViewName("ViewMember");
		mav.addObject("mem", result);
		// ViewMember.html 화면 띄움 (mem내용 result이름 전송)
		
		return mav;
	}
}







