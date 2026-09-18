package com.yse.dev.Book.DTO;

import lombok.Getter;
import lombok.Setter;

// "목록 표현"에 활용할 DTO
@Getter
@Setter
public class BookListDTO {
	private Integer bookId;
	private String title;
}
