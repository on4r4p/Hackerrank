import java.io.*;
import java.util.*;

public class Solution {
    public static Scanner scan = new Scanner(System.in);
    public static int B = scan.nextInt();
    public static int H = scan.nextInt();
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        if (B <= 0 || H <= 0){
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        else{
            System.out.println(B*H);
        }
        
        
        
    }
}
