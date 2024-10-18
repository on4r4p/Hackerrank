import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        List<Integer> L = Arrays.stream(sc.nextLine().split(" "))
        .map(Integer::parseInt).collect(Collectors.toList());
        int Q = sc.nextInt();sc.nextLine();
        for (int i = 0; i < Q; i++) {
            sc.nextLine();
            List<Integer> xy = Arrays.stream(sc.nextLine().split(" "))
            .map(Integer::parseInt).collect(Collectors.toList());
            if (xy.size() > 1){L.add(xy.get(0),xy.get(1));}
            else {L.remove((int) xy.get(0));}
        }
        System.out.println(
            L.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }
}
