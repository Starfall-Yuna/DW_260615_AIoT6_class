package com.yse.dev.book.Entity;

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

// JPA 구조 :: "DB테이블을 Java클래스처럼, DB데이터를 인스턴스(객체)처럼"
//		=> DB구조 - Java클래스구조(엔티티) 일관성있게 일치시키는 구조
// - Entity :: DB테이블 구조와 일치하는 클래스
//		(반드시 동일한 이름을 가진 테이블과 대조해보고, 구조가 다르면 오류 발생)

@Entity
@Data		// getter, setter, ... 자동 생성
@Builder	// 유연하고 편리하게 인스턴스 만드는 함수 생성
@NoArgsConstructor
@AllArgsConstructor
public class Book {
	@Id		// PK 지정
	@GeneratedValue(strategy = GenerationType.IDENTITY)
		// MySQL auto_increment 형식으로 값 자동 생성
	private Integer bookId;
	// (Java)bookId -> (MySQL)book_id
	
	@Column(length = 200)	// 칼럼 세부설정 (varchar 최대 크기)
	private String title;
	
	private int price;
	
	@CreationTimestamp		// 데이터 삽입한 시점의 날짜, 시간 자동 입력
	private LocalDateTime insertDateTime;
}
// spring.jpa.hibernate.ddl-auto = update
//		=> ddl의 일부인 create table 자동 생성+실행





