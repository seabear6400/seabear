package JAVA;

public class HELLOWORLD{
    
    /**
     * @param args
     */
    public static void main(String[] args){
         String Str;
        final StringBuilder sb = new StringBuilder("Hello");

        System.out.println(sb.append(" World!! "));
        System.out.println(sb.replace(5,6,""));
        System.out.println(sb.delete(8,9));
        System.out.println(sb.reverse());

    }

}
