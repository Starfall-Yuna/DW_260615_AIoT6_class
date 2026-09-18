package com.example.demo.Model;

// lombok :: 반복적 작성하는 코드를 자동 생성 어노테이션 모음
import lombok.Getter;
import lombok.Setter;

// 4개 멤버에 대해, get함수+set함수 코드 자동 생성
@Getter
@Setter
public class Score {
	private String name;
	private int java;
	private int mysql;
	private int sb;
	
	public Score(String n, int j, int m, int s) {
		this.name = n;
		this.java = j;
		this.mysql = m;
		this.sb = s;
	}
	
	public double average() {
		return (this.java+this.mysql+this.sb) / 3.0;
	}
}





