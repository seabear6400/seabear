package s21209_00;

public class S21209_00v2 {
	public static void main(String[] args) {
		
		
		int even = 0;
		int odd = 0;
		
		for(int cnt =1; cnt <11; cnt++) {
			
			if(cnt%2==0) {
				even +=cnt;
			}if(cnt%2==1) {
				odd +=cnt;
			}
		
			System.out.println("cnt :"+cnt+" sum : "+ (even+odd) +" even :"+even+" odd :"+odd);
		}
	 
	}
}
