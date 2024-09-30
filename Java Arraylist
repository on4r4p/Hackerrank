import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Output {
    public void getNum(List<List<Integer>> D,List<List<Integer>> X){
        for (List<Integer> sublist : X) {
            int y = sublist.get(0) - 1;
            int x = sublist.get(1) - 1;
            try {System.out.println(D.get(y).get(x));}
            catch (IndexOutOfBoundsException e) {System.out.println("ERROR!");}
        }
    }
};

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<List<Integer>> D = new ArrayList<>();
        List<List<Integer>> X = new ArrayList<>();
        int N = sc.nextInt();sc.nextLine();
        for (int i = 0; i < N; i++) 
            {D.add(Arrays.stream(sc.nextLine().trim().split("\\s+")).skip(1)
            .map(Integer::parseInt).collect(Collectors.toList()));}
        int Q = sc.nextInt();sc.nextLine();
        for (int i = 0; i < Q; i++) 
            {X.add(Arrays.stream(sc.nextLine().trim().split("\\s+"))
            .map(Integer::parseInt).collect(Collectors.toList()));}
        Output output = new Output();
        output.getNum(D,X);
        
    }
}
