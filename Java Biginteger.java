import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void println(String s) {System.out.println(s);}
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    BigInteger a = new BigInteger(scanner.nextLine());
    BigInteger b = new BigInteger(scanner.nextLine());
    println(a.add(b).toString());
    println(a.multiply(b).toString());
    }
}
