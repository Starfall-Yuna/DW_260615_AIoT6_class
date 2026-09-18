package com.example.demo.Controller;

// 자동 import :: Ctrl + Shift + o
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Service.ProductService;

// Controller 역할 :: 사용자 동작에 따른 행위를 "중재"
@Controller
public class ProductController {
	private final ProductService ps;
	public ProductController(ProductService p) {
		this.ps = p;
	}
	
	@GetMapping("/stock")		// "localhost:8080/stock" 링크 접속할 때,
	public String productHome() {
		return "productForm";	// productForm.html을 화면 띄움
	}
	
	@PostMapping("/view")	// "localhost:8080/view"(post방식) 링크 접속할 때,
	@ResponseBody
	public String viewStock(
			@RequestParam("productId") String pId) {
		// name이 productId인 태그의 입력값을, pId라는 이름으로 사용
		
		// 1. pId가 상품ID인 데이터의 재고량을 DB에서 조회 (Service)
		int rs = ps.viewProStock(pId);
		// 2. 사용자에게 표시할 내용 return (Controller)
		return pId+"의 현재 재고는 "+rs+"개입니다.";
	}
	
	@PostMapping("/plus")
	public ModelAndView plusStock(
			@RequestParam("productId") String pId,
			@RequestParam("amount") int amt,
			ModelAndView mav) {
		// 1. pId가 상품ID인 데이터의 재고량에 amt값을 더하는 DB 연산 수행 (Service)
		ps.plusProStock(pId, amt);
		
		// 2. ModelAndView 설정 (setViewName(), addObject())
		mav.setViewName("result");		// result.html 파일을 표시
		mav.addObject("proId", pId);	// pId값을 proId 이름으로 전송
		mav.addObject("amount", amt);	// amt값을 amount 이름으로 전송
		
		// 3. ModelAndView 반환
		return mav;
	}
	
	@PostMapping("/add")
	public ModelAndView addStock(
			@RequestParam("productId") String pId,
			@RequestParam("proName") String pName,
			@RequestParam("proStock") int pStock, 
			ModelAndView mav) {
		// 1. 3개의 값 기준으로, insert 수행 (Service)
		ps.insertProduct(pId, pName, pStock);
		
		// 2. ModelAndView 설정
		mav.setViewName("insert");
		mav.addObject("id", pId);
		mav.addObject("name", pName);
		mav.addObject("stock", pStock);
		//	사용자에게 insert.html 내용을 표시
		//	(pId값, pName값, pStock값을 각각 id, name, stock 이름으로 전송)
		
		// 3. ModelAndView 반환
		return mav;
	}
	
	@PostMapping("/remove")
	public ModelAndView removeStock(
			@RequestParam("productId") String pId,
			ModelAndView mav) {
		// 1. 입력받은 상품ID 데이터를 DB 삭제 수행 (Service)
		ps.deleteProduct(pId);
		
		// 2. ModelAndView 설정
		mav.setViewName("delete");
		mav.addObject("id", pId);
		// delete.html 사용자에게 표시 (pId값을 id 이름으로 전송)
		
		// 3. ModelAndView 반환
		return mav;
	}
}






