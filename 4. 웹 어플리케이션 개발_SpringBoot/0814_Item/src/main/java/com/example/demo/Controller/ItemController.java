package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.Model.Item;
import com.example.demo.Service.ItemService;

@Controller
public class ItemController {
	private final ItemService is;
	public ItemController(ItemService i) {
		this.is = i;
	}
	
	@GetMapping("/")
	public String home() {
		return "redirect:/item/list";
	}
	@GetMapping("/item/list")
	public ModelAndView itemList(ModelAndView mav) {
		// 1. 목록에 표현할 내용 가져오기 (Service)
		List<Item> result = is.getAllItem();
		
		// 2. ModelAndView 설정
		mav.setViewName("list");
		mav.addObject("r", result);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
	
	@GetMapping("/item/detail")
	public ModelAndView itemDetail(
			@RequestParam("item_num") int num,
			ModelAndView mav) {
		// 1. 특정 상품번호의 상품 정보 전체 조회 (Service)
		List<Item> result = is.getOneItem(num);
		
		// 2. ModelAndView 설정
		mav.setViewName("detail");
		mav.addObject("rt", result);
		
		// 3. ModelAndView 반환(실행)
		return mav;
	}
}




