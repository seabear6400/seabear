package s21209_00;

public class S201209_01v99 {

	public static void main(String[] args) {
		
		// 비교 연산자 : 문자열의 비교
		
		String str1 = "abd";
		String str2 = "abd";
		System.out.println("기본변수== :"+(str1==str2));
		System.out.println("기본변수equ :"+(str1.equals(str2)));
		
		String str3 = new String("abc");
		String str4 = new String("abc");
		System.out.println("참조변수== :"+(str3==str4));		// 문자열 비교에는 == 대신 equals()를 사용해야 한다. 
		System.out.println("참조변수equ :"+(str3.equals(str4)));
		
	}

}
