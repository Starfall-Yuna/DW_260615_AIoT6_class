package com.example.demo.Model;

import lombok.Getter;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Member {
	String memId;
	String memName;
	String memPw;
}

// @Getter(lombok) :: 아래 함수 코드 자동 생성
// getMemId() 	-> DB 조회한 데이터 중 id값 불러오는 함수
// getMemName() -> DB 조회한 데이터 중 name값 불러오는 함수
// getMemPw()	-> DB 조회한 데이터 중 passwd값 불러오는 함수

// @NoArgsConstructor :: 매개변수X 생성자 코드 자동 생성
// Member() {} -> 생성자
// @AllArgsConstructor :: 매개변수O 생성자 코드 자동 생성
// Member(String, String, String) -> 생성자
//		-> 3가지의 DB 데이터 기반으로 가공할 인스턴스값 설정