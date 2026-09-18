package com.example.demo.Service;

import com.example.demo.Application;
import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Todo;

@Service
public class TodoService {
	private final Application application;
	private final JdbcTemplate jp;
	public TodoService(JdbcTemplate j, Application application) {
		this.jp = j;
		this.application = application;
	}
	
	// todo 전체 데이터 조회
	// (사전에 필요한 값 :: X /
	//		결과값 :: DB테이블 전체 데이터(2개 이상의 데이터 쌍))
	public List<Todo> selectSQL1() {
		String sql = "select * from todo";
		
		// queryForObject() :: 데이터 한 쌍 결과로 받아올 때
		// *query() :: 데이터 2쌍 이상의 결과 받아올 때
		List<Todo> todoList = jp.query(
			sql,
			// DB조회데이터(rs) --(변환)--> Java인스턴스(Todo() 생성자)
			(rs, rowNum) -> new Todo (
				rs.getInt("id"),
				rs.getString("category"),
				rs.getString("content"),
				rs.getString("completed")
			)	// Todo테이블의 데이터 개수에 따라 총 3개의 인스턴스 생성
		);
		
		return todoList;
	}
	
	// 선택한 카테고리 데이터 조회
	// (사전에 필요한 값 :: 카테고리(target) /
	//		결과값 :: 검색된 데이터 전체 칼럼 내용)
	public List<Todo> FilterTodo(String target){
		if(target.equals("study") == true) {target="공부";}
		else if(target.equals("life") == true) {target="라이프";}
		else {target="업무";}
		
		String sql = """
				select * from todo
				where category = ?
				order by completed asc
				""";
		List<Todo> filter = jp.query(
			sql,
			(rs, ignored) -> new Todo(
				rs.getInt("id"),
				rs.getString("category"),
				rs.getString("content"),
				rs.getString("completed")
			),
			target
		);
		return filter;
	}
}








