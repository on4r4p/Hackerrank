

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest = s.substring(0,k);
        int lns = s.length();
        for (int i=0;i<=lns-k;i++){
            String sub = s.substring(i,i+k);
            if (sub.compareTo(largest) >= 0){
                largest = sub;
            }
            if (sub.compareTo(smallest) <=0){
                smallest= sub;
            }


 //       for (String subb: subLst){
 //           System.out.print(subb);
        }
        
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }

