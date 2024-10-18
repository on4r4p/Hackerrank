    import java.util.*;
    import java.util.stream.Collectors;
    public class test {
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            Deque<Integer> deque = new ArrayDeque<>();
            Map<Integer,Integer> cnt = new HashMap<>();
            
            int n = in.nextInt();
            int m = in.nextInt();
            int mx = 0;
            in.nextLine();
            
            List<Integer> A = Arrays.stream(in.nextLine().trim().split("\\s+"))
                    .map(Integer::parseInt).collect(Collectors.toList());
                    
            for (int i = 0; i < n; i++) {
                deque.addLast(A.get(i));
                cnt.put(A.get(i),cnt.getOrDefault(A.get(i), 0)+1);
                if (deque.size()>m) {
                    int rm = deque.removeFirst();
                    cnt.put(rm,cnt.get(rm)-1);
                    if (cnt.get(rm) == 0) cnt.remove(rm);   
                }
               if (deque.size()== m) mx = Math.max(mx,cnt.size());
            }
            System.out.println(mx);
        }
    }



