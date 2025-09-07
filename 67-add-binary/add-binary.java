class Solution {
    
    public String addBinary(String a, String b) {
        int carry = 0;
        String res = "";
        int m = a.length(), n = b.length(), i =m-1, j = n-1;
        while (i>=0 || j>=0) {
            char a1 = '0', b1 = '0';
            if (i>=0)
            a1 = a.charAt(i);
            if (j>=0)
            b1 = b.charAt(j);

            int ax = Character.getNumericValue(a1);
            int bx = Character.getNumericValue(b1);
            int curr;
            curr = (ax+bx+carry)%2;
            carry = (ax+bx+carry)/2;  
            res = String.valueOf(curr)+res;
            i--;
            j--;
        }
        if (carry == 1) {
            res = "1"+res;
        }
        return res;
    }
}