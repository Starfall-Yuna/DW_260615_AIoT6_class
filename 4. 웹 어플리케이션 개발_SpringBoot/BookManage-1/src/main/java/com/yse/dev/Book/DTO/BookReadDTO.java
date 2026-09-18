package com.yse.dev.Book.DTO;

import java.time.LocalDateTime;

import lombok.Getter;
import lombok.Setter;

// "책 조회"에 사용할 DTO (책 전체 내용)
@Getter
@Setter
public class BookReadDTO {
	private Integer bookId;
	private String title;
	private int price;
	private LocalDateTime insertDateTime;
}


