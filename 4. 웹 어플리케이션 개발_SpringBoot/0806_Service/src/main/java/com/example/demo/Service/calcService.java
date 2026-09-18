package com.example.demo.Service;

import org.springframework.stereotype.Service;

// Service :: 자주 쓰이고 필요한 "기능 구현"

@Service
public class calcService {
	public int executeAdd(int a, int b) {
		System.out.println("Service의 덧셈 연산 함수입니다.");
		return a+b;
	}
	public int executeCalc(int a, int b, String op) {
		if(op.equals("plus") == true) { return a+b; }
		else if(op.equals("minus") == true)	{ return a-b; }
		else if(op.equals("multi") == true)	{ return a*b; }
		else if(op.equals("division") == true)	{ return a/b; }
		else { return a%b; }
	}
}
