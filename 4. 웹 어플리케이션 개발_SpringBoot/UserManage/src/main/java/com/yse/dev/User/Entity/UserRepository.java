package com.yse.dev.User.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

// (ex) 내가 ""num칼럼의 값에 있어서 특정 값이 있는지 없는지만 판별""하는 기능을 만들려고 하는데
//		이때에 레포지토리에서 쓸 수 있는 함수는 어떤걸까?
public interface UserRepository extends JpaRepository<User, Integer> {
	// num칼럼에서 n의 값을 갖는 데이터 유무 판별 (있음(true) / 없음(false))
	public boolean existsByNum(Integer n);
}
