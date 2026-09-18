package com.yse.dev.book.dto;

import java.time.LocalDateTime;

import com.yse.dev.book.Entity.Book;

import lombok.Getter;

// 검색한 책의 책번호+책이름+책가격+데이터 생성시점 (4가지)
@Getter
public class BookReadDTO {
	private Integer bookId;
	private String title;
	private int price;
	private LocalDateTime insertDateTime;
	
	// DB 검색 데이터 -> Java 인스턴스 변환 (가공)
	// (사전에 필요한 값 :: DB 검색 데이터(b) / 결과값 :: Java 인스턴스)
	public BookReadDTO fromBook(Book b) {
		this.bookId = b.getBookId();
		this.title = b.getTitle();
		this.price = b.getPrice();
		this.insertDateTime = b.getInsertDateTime();
		return this;
	}
}
