package Model;

public class Book {
	public String book_name;
	public String author;
	public String isbn;

	public Book(String n, String a, String i) {
		// DB 데이터를 매개변수로 받아서
		// 여기서 한 묶음씩 묶는 가공 작업
		this.book_name = n;
		this.author = a;
		this.isbn = i;
	}
}
