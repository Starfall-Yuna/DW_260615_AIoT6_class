package com.yse.dev.Book.DTO;

import jakarta.validation.constraints.Positive;
import lombok.Getter;
import lombok.NonNull;
import lombok.Setter;

// "책 생성"을 위한 DTO
@Getter
@Setter
public class BookCreateDTO {
	@NonNull
	private String title;
	
	@Positive
	private int price;
}
