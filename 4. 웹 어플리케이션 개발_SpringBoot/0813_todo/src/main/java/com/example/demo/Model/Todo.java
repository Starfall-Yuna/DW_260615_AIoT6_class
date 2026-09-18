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

//	@AllArgsConstructor로 자동 생성된 코드
//public Todo(int i, String cate, String c, String com) {
//	this.id = i;
//	this.category = cate;
//	this.content = c;
//	this.completed = com;
//}

// @Getter로 자동 생성된 코드
//public int getId() {
//	return id;
//}
//public String getCategory() {
//	return category;
//}
//public String getContent() {
//	return content;
//}
//public String getCompleted() {
//	return completed;
//}
