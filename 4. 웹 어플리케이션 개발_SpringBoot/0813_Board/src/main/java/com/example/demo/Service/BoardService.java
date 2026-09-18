package com.example.demo.Service;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Board;

@Service
public class BoardService {
	private final JdbcTemplate jtl;
	public BoardService(JdbcTemplate j) {
		this.jtl = j;
	}
	
	// 목록에 표시할 내용 가져오기
	// (사전에 필요한 값 :: X /
	//	결과값 :: 전체 게시판 내용(일부 칼럼))
	public List<Board> getAll(){
		String sql = """
				select id, title, writer
				from board
				""";
		List<Board> result = jtl.query(
			sql,
			// select문 조회결과 rs 가져오기
			// rs값을 Java에서 사용O 가공 (Model인 Board 생성자)
			(rs, ignored) -> new Board(
				rs.getInt("id"),
				rs.getString("title"),
				rs.getString("writer"),
				null
			)
		);
		return result;
	}
	
	// 특정ID값인 게시판의 모든 내용 조회
	// (사전에 필요한 값 :: 조회할 게시판번호(int)/
	//		결과값 :: 해당 게시판(Board)의 모든 칼럼 내용)
	public List<Board> getContent(int target){
		String sql = """
				select * from board
				where id = ?
				""";
		List<Board> dt = jtl.query(
			sql,
			// select문 결과를 rs 이름으로 받아옴
			// 	"가공" :: DB데이터(rs) -> Java형식(Board)으로 변형
			(rs, ignored) -> new Board(
				rs.getInt("id"),
				rs.getString("title"),
				rs.getString("writer"),
				rs.getString("content")
			),
			target
		);
		
		return dt;
	}
}








