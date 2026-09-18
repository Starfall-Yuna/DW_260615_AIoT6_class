package com.yse.dev.book.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

// - Repository :: 지정된 Entity 테이블의 sql문 자동 생성

// JpaRepository<T, ID>		(T :: 엔티티 이름, ID :: PK (클래스형) 자료형)
public interface BookRepository extends JpaRepository<Book, Integer> {

}
