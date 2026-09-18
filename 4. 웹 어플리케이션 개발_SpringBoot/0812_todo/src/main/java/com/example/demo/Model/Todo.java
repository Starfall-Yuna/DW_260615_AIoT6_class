package com.example.demo.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class Todo {
	private int id;
	private String category;
	private String content;
	private String completed;
}
