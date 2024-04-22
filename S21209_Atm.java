package s21209_java04;

import java.util.Scanner;

public class S21209_Atm {

	static int bankAcount;
	int account;
	int n;
	
	public static void main(String[] args) {
		S21209_Atm a = new S21209_Atm();
		S21209_Atm b = new S21209_Atm();
		
		do {
			Scanner scan = new Scanner(System.in);
			
			System.out.println("메뉴 선택 : 1.입금 2.출금 9.종료");
			int selectMenu = scan.nextInt();
			if(selectMenu == 9){
				break;
			}
			if(selectMenu < 1 || selectMenu > 2) {
				continue;
			}if(selectMenu==1) {
				System.out.println("계좌 선택: 전메뉴 = 0, 카카오=1, 국민=2");
				int num = scan.nextInt();
				if(num==1){
					System.out.print("금액을 입력하세요: ");
					int n = scan.nextInt();
					a.account += n;
					bankAcount += a.account;
					System.out.println("A잔액: "+a.account+"총금액: "+bankAcount);
					System.out.println("B잔액: "+b.account+"총금액: "+bankAcount);
					System.out.println(bankAcount);
				}else if(num==2){
					int n = scan.nextInt();
					b.account -= n;
					bankAcount += b.account;
					System.out.print("금액을 입력하세요: ");
					System.out.println("A잔액: "+a.account+"총금액: "+bankAcount);
					System.out.println("B잔액: "+b.account+"총금액: "+bankAcount);
					System.out.println(bankAcount);
				}else {
					continue;
				}
			}if(selectMenu==2) {
				System.out.println("계좌 선택: 전메뉴 = 0, 카카오=1, 국민=2");
				int num = scan.nextInt();
				int n = scan.nextInt();
				if(num==1){
					System.out.print("금액을 입력하세요: ");
					a.account -= n;
					bankAcount -= a.account;
					System.out.println("A잔액: "+a.account+"총금액: "+bankAcount);
					System.out.println("B잔액: "+b.account+"총금액: "+bankAcount);
					System.out.println(bankAcount);
				}else if(num==2){
					System.out.print("금액을 입력하세요: ");
					b.account -= n;
					bankAcount -= b.account;
					System.out.println("A잔액: "+a.account+"총금액: "+bankAcount);
					System.out.println("B잔액: "+b.account+"총금액: "+bankAcount);
					System.out.println(bankAcount);
				}
			}
		}while(true); 
		
	}
}

