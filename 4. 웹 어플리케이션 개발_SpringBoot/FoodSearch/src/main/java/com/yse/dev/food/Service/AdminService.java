package com.yse.dev.food.Service;

import org.springframework.stereotype.Service;

import com.yse.dev.food.DTO.AdminAccessDTO;
import com.yse.dev.food.Entity.AdminRepository;

@Service
public class AdminService {
	private final AdminRepository ar;
	public AdminService(AdminRepository a) {
		this.ar = a;
	}
	
//	String input_id,
//	String input_pw		=> AdminAccessDTO	
	// 입력받은 id/pw가 테이블에 있는 내용인지 확인
	public Boolean isLogin(AdminAccessDTO aa) {
		// Admin 테이블에 input_id-input_pw 계정 정보가 존재하면 -> result=true;
		// Admin 테이블에 input_id-input_pw 계정 정보가 존재X -> result=false;
		Boolean result = ar.existsByIdAndPw(aa.getId(), aa.getPw());
		return result;
	}
}
