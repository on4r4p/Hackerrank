

    static boolean isAnagram(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        int lena = a.length();
        int lenb = b.length();
        
        int[] taba = new int[26];
        int[] tabb = new int[26];
        
        if (lena != lenb) {
            return false;
        }
        
        for (int i = 0; i < lena; i++) {
               char Ca = a.charAt(i);
               char Cb = b.charAt(i);
               taba[Ca - 'a']++;
               tabb[Cb - 'a']++;
        }
        for (int i = 0; i < tabb.length; i++) {
            if (taba[i] != tabb[i]) {
                return false;
            }
        }
        return true;
    }

