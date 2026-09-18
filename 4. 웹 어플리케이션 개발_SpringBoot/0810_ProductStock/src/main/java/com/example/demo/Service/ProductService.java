package com.example.demo.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class ProductService {
	// JdbcTemplate (DB sql 실행, 실행결과 받아옴)
	private final JdbcTemplate jt;
	public ProductService(JdbcTemplate j) {
		this.jt = j;
	}
	
	// 특정 상품ID인 데이터의 재고량을 DB에서 조회
	// (필요한 값 :: 상품ID(proId), 결과 :: 재고량(int))
	public int viewProStock(String proId) {
		String sql = "select stock from product where id = ?";
		int result = jt.queryForObject(
			sql, Integer.class, proId
		);
		return result;
	}
	
	// 특정 상품ID인 데이터의 재고량에 임의의 값을 더하는 DB 연산 수행
	// (필요한 값 :: 상품ID(proId), 추가할 재고량(a)
	public void plusProStock(String proId, int a) {
		String sql = "update product set stock = stock+? where id = ?";
		jt.update(
			sql, a, proId
		);
	}
	
	// 3개의 값 기준으로, insert 수행
	// (필요한 값 :: 상품ID(proId), 상품명(proName), 재고량(proStock))
	public void insertProduct(String proId, String proName, int proStock) {
		String sql = "insert into product values (?, ?, ?)";
		jt.update(
			sql, proId, proName, proStock
		);
	}
	
	// 특정 상품ID 데이터 delete 수행
	// (필요한 값 :: 상품ID(proId))
	public void deleteProduct(String proId) {
		String sql = "delete from product where id = ?";
		jt.update(
			sql, proId
		);
	}
}






