public class MinimumValue{
    
    static int min(int[] a) {
        int min = a[0];
        for(int i=1;i<a.length;i++) {
            if(a[i]< min) {
                min = a[i];
            }
            
        }
        return min;
    }
    
    public static void main(String[] args) {
        int[] a = {-2, -11, 0 , 1, 7, 6};
        System.out.println(min(a));
    }
    
}
