package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Score;

@Service
public class ScoreService {
	private final JdbcTemplate jt;
	public ScoreService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// 입력받은 학생의 전체 칼럼 조회 결과 불러오는 select문 수행
	// (필요한 값 :: 학생의 이름
	//		결과값 :: 검색한 학생의 전체 칼럼 데이터 한 쌍 (1쌍, 4개)	-> Score 인스턴스
	public Score searchSQL(String stuName) {
		// 1. select sql문 작성
		String sql = """
				select *
				from score
				where name = ?
				""";
		// 2. sql문 실행 + 결과 가져오기(!!!)
		// 	(1) 실행할 sql문
		//  (2) sql문 실행한 결과를 어떻게 처리할지...	-> 가공방식 결정
		//		rs라는 이름으로 select문 검색 결과 불러오기
		//		rs의 결과 하나하나를 Score 모델을 통해 한 묶음씩 묶기 (인스턴스 생성)
		//  (3) sql문 보충
		Score result = jt.queryForObject(
			sql,
			(rs, rowNum) -> new Score(
					rs.getString("name"),
					rs.getInt("java"),
					rs.getInt("mysql"),
					rs.getInt("springboot")
			),
			stuName
		);
		// result에 DB select문 실행결과 저장
		
		return result;
	}
	
	// 입력받은 값들 기준, score 테이블에 insert문 수행
	// (필요한 값 :: score 칼럼값(name, 성적 3개),
	// 		결과값 :: X )
	public void insertSQL(String n, int sc1, int sc2, int sc3) {
		String sql = "insert into score values (?, ?, ?, ?)";
		jt.update(
			sql, n, sc1, sc2, sc3
		);
	}
	
	// 입력받은 이름의 학생 평균 조회
	// (필요한 값 :: 학생 이름,
	//		결과값 :: 성적 3개에 대한 평균값)
	public double searchAvg(String stuName) {
		String sql = """
				select *
				from score
				where name = ?
				""";
		Score result = jt.queryForObject(
			sql,
			(rs, rowNum) -> new Score(
				rs.getString("name"),
				rs.getInt("java"),
				rs.getInt("mysql"),
				rs.getInt("springboot")
			),
			stuName
		);
		
		return result.average();
	}
}








