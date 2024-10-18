import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Hourglass{
    private int[][] nlst;
    public Hourglass(List<List<Integer>> arr){
        nlst = arr.stream()
                  .map(list -> list.stream().mapToInt(Integer::intValue).toArray())
                  .toArray(int[][]::new);    
    }   
    public int[][] getNlst() {return nlst.clone();}
    public List<Integer> sumUp(int needle){
        int[] up = nlst[needle];
        int[] mid = nlst[needle + 1];
        int[] bottom = nlst[needle + 2];      
        int[] sumup = new int[up.length - 2];
        int[] sumid = new int[mid.length - 2];
        int[] sumbot = new int[bottom.length - 2];

        for (int i = 0; i < sumup.length; i++)
            {sumup[i] = up[i] + up[i + 1] + up[i + 2];}
        for (int i = 0; i < sumid.length; i++)
            {sumid[i] = mid[i + 1];}
        for (int i = 0; i < sumbot.length; i++)
            {sumbot[i] = bottom[i] + bottom[i + 1] + bottom[i + 2];}

        List<Integer> sumhourglass = new ArrayList<>();
        for (int n = 0; n < sumup.length; n++) {
            sumhourglass.add(sumup[n] + sumbot[n] + sumid[n]);}
        return sumhourglass;    
    }
}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        List<List<Integer>> arr = new ArrayList<>();
        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine()
                        .replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList()));
            } catch (IOException ex) {throw new RuntimeException(ex);}
        });
        bufferedReader.close();
        
        Hourglass sandwatch = new Hourglass(arr);
        ArrayList<Integer> sumList = new ArrayList<>();
        for (int i = 0; i < (sandwatch.getNlst().length - 2); i++) {
            sumList.addAll(sandwatch.sumUp(i));}
        System.out.println(Collections.max(sumList));
    }
}
