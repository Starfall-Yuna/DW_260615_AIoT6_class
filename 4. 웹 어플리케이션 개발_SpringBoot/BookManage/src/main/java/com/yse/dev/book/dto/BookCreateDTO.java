package com.yse.dev.book.dto;

import jakarta.validation.constraints.Positive;
import lombok.Getter;
import lombok.NonNull;
import lombok.Setter;

// - DTO :: 파일 간의 데이터 전달 매개체
// 	BookCreateDTO -> "책 생성에 필요한" 데이터 전달에 활용
@Getter
@Setter
public class BookCreateDTO {
	@NonNull	// not null 유사
	private String title;
	
	@Positive	// 양수의 값을 가져야함
	private int price;
}
