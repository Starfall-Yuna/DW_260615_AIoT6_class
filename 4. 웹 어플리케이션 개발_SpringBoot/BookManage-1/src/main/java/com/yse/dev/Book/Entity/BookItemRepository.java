package com.yse.dev.Book.Entity;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

public interface BookItemRepository extends JpaRepository<BookItem, Integer> {
	// title항목을 포함하는 책 제목 검색에 활용할 함수
	List<BookItem> findByTitleContaining(String title);
	
	// findByTitleContaining
	// findTopByOrderByPriceDesc
	
}
