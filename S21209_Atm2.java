package s21209_java04;

import java.util.Scanner;

public class S21209_Atm2 {
   static int bankAcount;
   int acount;
   
   public S21209_Atm2() {
      bankAcount = 0; //a , b
      acount = 0;
   }
   public S21209_Atm2(int BA, int AC) {
      
   }
   
   
   public static void main(String[] args) {
      // 참조 변수
      S21209_Atm2 a = new S21209_Atm2();
      S21209_Atm2 b = new S21209_Atm2();
      
   do {
      Scanner scan = new Scanner(System.in);
      // 메뉴 선택 창
      System.out.println("\r메뉴 선택 : 1. 입금  2. 출금  9. 종료");
      int selectMenu = scan.nextInt();
      
      
      // 나가기 창
      if(selectMenu == 9) {
         System.out.println("이용해주셔서 갑사합니다 ^^7");
         break;
      }
      // 다른 숫자 입력
      if(selectMenu < 1 || selectMenu > 2) {
         System.out.println("정확한 숫자를 입력해주세요.");
         continue; // 다시 메뉴로 돌아감
         } 
//      	System.out.println("금액을 입력");
//      	int money = scan.nextInt();
      	
      	if (selectMenu == 1) { // 입금 시작
            System.out.println("계좌 선택 : 전메뉴=0  A=1  B=2  종료=9  ");
            int accountmenu = scan.nextInt();
            
            if(accountmenu == 1) {
               System.out.println("금액 입력 : ");
               int amount = scan.nextInt();
               bankAcount += amount;
               a.acount += amount;
            } else if(accountmenu == 2) {
               System.out.println("금액 입력 : ");
               int amount = scan.nextInt();
               bankAcount += amount;
               b.acount += amount;
            } else if(accountmenu == 9) {
               System.out.println("이용해주셔서 갑사합니다 ^^7");
               break;
            }
            else if(accountmenu == 0) {
               System.out.println("전 메뉴로 돌아갑니다.");
               continue;
            }
         }// 입금 끝
            
         // 출금 시작
         else if (selectMenu == 2) {
            System.out.println("계좌 선택 : 전메뉴=0  A=1  B=2  종료=9  ");
            int inputaccount = scan.nextInt();
            if(inputaccount == 0) {
               continue;
            }
            if(inputaccount == 1) {
               System.out.println("금액 입력 : ");
               int amount = scan.nextInt();
               bankAcount -= amount;
               a.acount -= amount;
               }
            else if(inputaccount == 2) {
               System.out.println("금액 입력 : ");
               int amount = scan.nextInt();
               bankAcount -= amount;
               b.acount -= amount;
               }
//                  
         }
         
            
      
      
      } while (true);
   
      
   
   
   
      }
         
   }

