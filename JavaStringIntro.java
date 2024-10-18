import java.io.*;
import java.util.*;
import java.lang.Math;
public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        System.out.println(A.length()+B.length());
//        for (int i=0;i<=Math.max(A.length(),B.length());i++)
        //String bool = "No";
        //if (A.length() >= B.length()){
            //for (int i = 0; i<=A.length();i++){
               // char ca = A.charAt(i);
                //for (int j=i;j<=B.length();j++){
                 //   char cb = B.charAt(j);
                //    if (ca != cb && ){
                        
                    
              //      }
            //    }
               
          //  }
        //}
        
        int alphaChk = A.compareTo(B);
        if (alphaChk <0){
            System.out.println("No");
        }
        else if (alphaChk > 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        String Acap = A.substring(0,1).toUpperCase() + A.substring(1);
        String Bcap = B.substring(0,1).toUpperCase() + B.substring(1);
        System.out.println(Acap+" "+Bcap);
        
        
    }
}



