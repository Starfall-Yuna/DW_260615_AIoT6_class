package com.example.demo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Score;
import com.example.demo.Service.ScoreService;

@Controller
public class ScoreController {
	private final ScoreService ss;
	public ScoreController(ScoreService s) {
		this.ss = s;
	}
	
	@GetMapping("/")				// "localhost:8080" 접속하면,
	public String home() {
		return "redirect:/score";	// "localhost:8080/score" 방향 재설정
	}
	@GetMapping("/score")			// "localhost:8080/score" 접속하면,
	public String scoreHome() {
		return "scoreForm";			// scoreForm.html 화면 띄움
	}
	
	@PostMapping("/search")
	public ModelAndView searchScore(
			@RequestParam("stuName") String stuName,
			ModelAndView mav) {
		// 1. 입력받은 학생의 전체 칼럼 조회 결과 불러오기 (Service)
		Score sr = ss.searchSQL(stuName);	// sr에 조회결과 저장
		
		// 2. ModelAndView 설정
		mav.setViewName("select");
		mav.addObject("name", sr.getName());
		mav.addObject("java", sr.getJava());
		mav.addObject("mysql", sr.getMysql());
		mav.addObject("springboot", sr.getSb());
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
	
	@PostMapping("/insert")
	public ModelAndView insertScore(
			@RequestParam("name") String stuName,
			@RequestParam("java") int java,
			@RequestParam("mysql") int mysql,
			@RequestParam("sb") int springboot,
			ModelAndView mav) {
		// 1. 입력받은 값들 기준, insert문 수행 (Service)
		ss.insertSQL(stuName, java, mysql, springboot);
		
		// 2. ModelAndView 설정
		mav.setViewName("insert");
		mav.addObject("Name", stuName);
		mav.addObject("java", java);
		mav.addObject("mysql", mysql);
		mav.addObject("sb", springboot);
		// insert.html 파일을 화면에 띄움
		// (stuName값을 Name 이름으로 전송)
		// (springboot값을 sb 이름으로 전송)
		// ...
		
		// 3. ModelAndView 반환
		return mav;
	}
	
	@PostMapping("searchAvg")
	public ModelAndView searchAvg(
			@RequestParam("stuName") String stuName,
			ModelAndView mav) {
		// 1. 입력받은 이름의 학생 평균 조회 (Service)
		double avg = ss.searchAvg(stuName);
		
		// 2. ModelAndView 설정
		mav.setViewName("average");
		mav.addObject("result", avg);
		
		// 2. ModelAndView 반환
		return mav;
	}
}





