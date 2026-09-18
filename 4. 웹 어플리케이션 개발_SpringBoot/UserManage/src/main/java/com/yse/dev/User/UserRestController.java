package com.yse.dev.User;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.yse.dev.User.Service.UserService;

@RestController
public class UserRestController {
	private final UserService us;
	public UserRestController(UserService u) {
		this.us = u;
	}
	
	// localhost:8080/api/user/3  (uId = 3)
	@GetMapping("/api/user/{userId}")
	public ResponseEntity<Boolean> searchUser(@PathVariable("userId") Integer uId) {
		boolean ex = us.search(uId);
		
		if(ex == true) {	// 데이터가 존재할 때 -> 200 처리
			return ResponseEntity.ok(true);
		}
		else {		// 데이터가 존재하지 않을 때 -> 404 처리
			return ResponseEntity
					.status(HttpStatus.NOT_FOUND)
					.build();
		}
	}
}





