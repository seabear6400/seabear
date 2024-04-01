package s21209_00;

public class S201209_01v100 {

	public static void main(String[] args) {
		
		double pi = 3.141592;
		
		System.out.println("result1 :" + Math.round(pi));
		System.out.println("result2 :" + pi);
		System.out.println("result3 :" + pi*1000);
		System.out.println("result4 :" + (Math.round(pi*1000)));
	    System.out.println("result5: " + (((double)Math.round((pi*1000))/1000)));
	    System.out.println("result6: " + (((int)(pi*1000)/1000.0)));
		
	}

}
