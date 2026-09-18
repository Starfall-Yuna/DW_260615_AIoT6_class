package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class LoginService {
	// JdbcTemplate 인스턴스 생성 (자동으로 (쓸수있는 형태로) 초기화)
	private final JdbcTemplate jt;
	public LoginService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// 입력받은 id, passwd 기반으로, DB에 데이터 존재하는지 확인 -> 로그인 가능 여부 확인
	public boolean checkLogin(String id, String passwd) {
		String sql = "select count(*) from member where id = ? AND pw = ?";
		// 로그인 가능 -> sql 결과값 :: 1 이상
		// 로그인 불가능 -> sql 결과값 :: 0
		
		// sql문 완성 -> sql문 DB 실행 -> 실행결과 가져오기
		Integer count = jt.queryForObject(
			sql, Integer.class, id, passwd
		);
		
		if(count == 0) {return false;}
		else {return true;}
	}
	
	public void joinMember(String id, String pw, String name) {
		String sql = "insert into member values (?, ?, ?);";
		
		jt.update(
			sql, id, pw, name
		);
	}
}
