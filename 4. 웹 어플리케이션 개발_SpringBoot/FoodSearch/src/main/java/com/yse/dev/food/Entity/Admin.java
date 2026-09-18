package com.yse.dev.food.Entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
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
public class Admin {
	// 칼럼 구성 :: id(아이디, PK), pw(비밀번호), name(사용자명)
	
	@Id
	@Column(length = 200)
	private String id;
	
	@Column(length = 200)
	private String pw;
	
	@Column(length = 200)
	private String name;
}




