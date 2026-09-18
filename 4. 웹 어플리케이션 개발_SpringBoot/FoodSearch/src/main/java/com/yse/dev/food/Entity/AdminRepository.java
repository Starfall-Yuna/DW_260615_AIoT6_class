package com.yse.dev.food.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

// 사용자에게 입력받은 아이디와 비밀번호에 대해서, 이게 DB의 테이블로 있는지 확인을 하려고 하는데, 이때 필요한 레포지토리의 함수가 뭘까?
// (DB테이블에서 아이디를 저장하는 칼럼은 id, 비밀번호를 저장하는 칼럼은 pw야.
//		그리고 결과값은 존재하는지에 대한 여부만 보고 싶으니 Boolean으로 받고 싶어.)
public interface AdminRepository extends JpaRepository<Admin, String> {
	public Boolean existsByIdAndPw(String id, String pw);
}
