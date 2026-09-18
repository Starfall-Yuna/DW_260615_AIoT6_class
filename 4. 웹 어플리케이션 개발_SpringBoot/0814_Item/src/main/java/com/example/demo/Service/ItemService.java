package com.example.demo.Service;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.demo.Model.Item;

@Service
public class ItemService {
	private final JdbcTemplate jt;
	public ItemService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// 목록(상품번호, 상품명)에 표현할 데이터 조회
	// (사전에 필요한 값 :: X /
	// 		결과값 :: 모든 상품 정보의 상품번호, 상품명)
	public List<Item> getAllItem(){
		String sql = """
				select item_num, name
				from item
				""";
		List<Item> itemList = jt.query(
			sql,
			// DB 조회 데이터(res) --(변환)--> Java 사용O 변환(Item)
			(res, ignored) -> new Item(
				res.getInt("item_num"),
				res.getString("name"),
				0,
				null,
				null
			)
		);
		return itemList;
	}
	
	// 특정 상품번호의 상품 정보 전체 조회
	// (사전에 필요한 값 :: 상품번호(int) 
	// 		/ 결과값 :: 검색 상품 전체 칼럼 내용)
	public List<Item> getOneItem(int number){
		String sql = """
				select * from item
				where item_num = ?
				""";
		List<Item> itemDetail = jt.query(
			sql,
			// DB조회데이터(res) --(변환)--> Java 사용O 형태(Item.class)
			(res, ignored) -> new Item(
				res.getInt("item_num"),
				res.getString("name"),
				res.getInt("low_price"),
				res.getString("image_link"),
				res.getString("item_page")
			), 
			number
		);
		return itemDetail;
	}
}








