import java.util.*;

public class Solution {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        //java8
        ArrayList<Integer> A = new ArrayList<>();
        while (scan.hasNextInt())A.add(scan.nextInt());
        int[] a = A.stream().mapToInt(i -> i).toArray();
        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
