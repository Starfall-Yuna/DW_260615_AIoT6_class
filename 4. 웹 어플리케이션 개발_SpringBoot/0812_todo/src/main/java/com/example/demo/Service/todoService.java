package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Todo;

@Service
public class todoService {
	private final JdbcTemplate jp;
	public todoService(JdbcTemplate j) {
		this.jp = j;
	}
	
	// Id를 통해서, 할일 데이터 조회하는 기능
	// (사전에 필요한 값 :: 임의의 Id(target))
	// (결과값 :: 할일 데이터())
	public Todo searchTodoById(int target) {
		String sql = "select * from todo where id = ?";
		Todo result = jp.queryForObject(
			sql,
			// Mysql데이터(rs) -> Java데이터(Todo형식으로 생성)
			(rs, ignored) -> new Todo(
				rs.getInt("id"),
				rs.getString("category"),
				rs.getString("content"),
				rs.getString("completed")
			), 
			target
		);	// result에 DB조회결과 저장
		return result;
	}
	
	// 전체 데이터 중, 미완료된 데이터 개수 조회
	// (사전에 필요한 값 :: X)
	// (결과값 :: 조회된 데이터 개수(int))
	public int countSQL() {
		String sql = "select count(*) from todo where completed = 'N'";
		int cnt = jp.queryForObject(sql, Integer.class);
		return cnt;
	}
}




