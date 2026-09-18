package com.yse.dev.User;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {
	@GetMapping("user/search")
	public String searchHome() {
		return "user/search";
	}
}
