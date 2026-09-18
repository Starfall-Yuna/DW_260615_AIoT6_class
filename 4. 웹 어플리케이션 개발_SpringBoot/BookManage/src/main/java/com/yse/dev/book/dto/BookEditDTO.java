package com.yse.dev.book.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Positive;
import lombok.Getter;
import lombok.NonNull;
import lombok.Setter;

@Getter
@Setter
public class BookEditDTO {
	@NonNull
	@Positive
	private Integer bookId;
	// not null, 양수(+)
	
	@NonNull
	@NotBlank
	private String title;
	// not null, 공백("") 안됌
	
	@NonNull
	@Min(1000)
	private int price;
	// not null, 1000 이상
}
