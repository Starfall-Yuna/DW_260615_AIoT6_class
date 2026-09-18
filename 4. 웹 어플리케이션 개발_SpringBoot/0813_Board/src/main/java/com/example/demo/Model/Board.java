package com.example.demo.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
	// New Board() 자동 생성
public class Board {
	private int id;
	private String title;
	private String writer;
	private String content;
}
