import java.util.Scanner;

public class StringOperator
{
public static void main(String args[])
{
int i;
String s1;

    int c[] = new int[120];
    Scanner sc = new Scanner(System.in);
    
    System.out.print("Enter a String to count alphabet: ");
    s1=sc.nextLine();
    
     for (i = 0; i < s1.length(); i++) {
        c[(int) s1.charAt(i)]++;
    }
  
    for (i = 0; i < 256; i++) {
        if (c[i] != 0) {
              System.out.println((char) i  + " :" + c[i] );
        }
   }
}
}



