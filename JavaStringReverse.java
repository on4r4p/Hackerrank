import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B ="";
        /* Enter your code here. Print output to STDOUT. */
        Integer ln=A.length();
        //System.out.println(A);
        //System.out.println(ln);
        for (int i = ln-1; i >= 0; i--) {
            char C = A.charAt(i);
            B = B + C;
        }
        //System.out.println(B);
        if (A.equals(B)) {
           System.out.println("Yes"); 
        } else {
           System.out.println("No"); 
        }
    }
}



