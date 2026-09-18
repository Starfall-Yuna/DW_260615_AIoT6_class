package com.example.demo.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class Item {
	private int item_num;
	private String name;
	private int low_price;
	private String image_link;
	private String item_page;
}
