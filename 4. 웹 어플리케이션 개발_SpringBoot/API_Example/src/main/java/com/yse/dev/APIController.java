package com.yse.dev;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class APIController {
	@GetMapping("/api")
	public String home() {
		return "list";
	}
	
	@GetMapping("/shop")
	public String shopHome() {
		return "shop";
	}
	
	@GetMapping("/shop/search")
	public String shopSearch() {
		return "search";
	}
}




