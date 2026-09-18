package com.yse.dev.User.Service;

import org.springframework.stereotype.Service;

import com.yse.dev.User.Entity.UserRepository;

@Service
public class UserService {
	private final UserRepository ur;
	public UserService(UserRepository u) {
		this.ur = u;
	}
	
	// 계정번호에 따른 사용자 정보 탐색 -> 있다(true)/없다(false) 판별
	public Boolean search(Integer number) {
		boolean result = ur.existsByNum(number);
		return result;
	}
}
