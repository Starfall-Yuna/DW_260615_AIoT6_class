package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class scoreController {
	@GetMapping("/input_score")		// localhost:8080/input_score로 접속하면,
	public String inputForm() {
		return "inputForm";			// inputForm.html 불러오기
	}
	
	@PostMapping("/calc_score")
	public ModelAndView calcScore(
			@RequestParam("n") String name,
			@RequestParam("d") int data,
			@RequestParam("net") int network, 
			@RequestParam("e") int embeded,
			ModelAndView mav) {
		// * 평균값 구하기
		double avg = (data + network + embeded) / 3.0;
		
		// * 평균에 따른 학점 구하기
		char score;
		if(90 <= avg && avg <= 100) { score = 'A'; }
		else if(80 <= avg && avg < 90) { score = 'B'; }
		else if(70 <= avg && avg < 80) { score = 'C'; }
		else if(60 <= avg && avg < 70) { score = 'D'; }
		else { score = 'F'; }
		
		// * 이름, 평균값, 학점값 .html 파일로 넘겨주기
		mav.setViewName("resultForm");	// resultForm.html 불러옴
		mav.addObject("name", name);
		mav.addObject("average", avg);
		mav.addObject("score", score);
		
		return mav;
	}
}

