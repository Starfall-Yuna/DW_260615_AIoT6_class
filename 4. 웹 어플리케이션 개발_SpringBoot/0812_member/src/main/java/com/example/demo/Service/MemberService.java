package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Member;

@Service
public class MemberService {
	private final JdbcTemplate jdbc;
	public MemberService(JdbcTemplate jp) {
		this.jdbc = jp;
	}
	
	// DB에 저장된 Member 데이터 총 개수 조회하는 기능
	public int countSQL() {
		String sql = "select count(*) from member";
		// queryForObject(실행할 sql문, 조회결과 처리할 방법(클래스 타입))
		int result = jdbc.queryForObject(sql, Integer.class);
		// result :: member 테이블의 데이터 총 개수 저장
		return result;
	}
	
	// 특정 ID를 가진 사용자 정보 조회
	// (사전에 필요한 값) ID값
	// (결과값) 전체 칼럼에 대한 사용자 정보 (1쌍, 3개)
	public Member searchSQL(String tg) {
		String sql = "select * from member where id = ?";
		// DB데이터 가공한 결과를 mem 저장
		Member mem = jdbc.queryForObject(
			sql,
			// rs(DB조회결과) ->
			//	[Java에서 쓸수있게끔] Member 인스턴스 가공
			(rs, rowNum) -> new Member(
				rs.getString("id"),		// id칼럼값 -> Member memId 설정
				rs.getString("name"),
				rs.getString("passwd")
			),
			tg
		);
		return mem;
	}
}










