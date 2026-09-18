package com.example.demo.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;

// (DTO) DB데이터 한쌍씩 담기 위한 상자
@Getter
@AllArgsConstructor
public class Book {
	private String book_id;
	private String name;
	private int price;
}

//@Getter
//public String getBook_id(){
//	return this.book_id;
//}
// ...
//@AllArgsConstructor
//public Book(String b, String n, int p) {
//	this.book_id = b;
//	this.name = n;
//	this.price = p;
//}


