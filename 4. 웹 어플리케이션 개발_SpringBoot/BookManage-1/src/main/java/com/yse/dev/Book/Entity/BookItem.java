package com.yse.dev.Book.Entity;

import java.time.LocalDateTime;

import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BookItem {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer bookId;		// PK, auto_increment(자동 값 생성)
	
	@Column(length = 200)
	private String title;		// varchar(200)
	
	private int price;
	
	@CreationTimestamp
	private LocalDateTime insertDateTime;	// 데이터 생성시점 시간 자동입력
}