public class Sortedclass {

    /**
     * Function that will tell if an input array is sorted 
     */
    static boolean isSorted(int[] a) { 
	if (a.length <2) {
		return true;
	}
	for (int i=1; i < a.length; i++) {
		if(a[i]<a[i-1]) {
			return false;
		}
	
	}
        return true;
    }
    

public static void main(String[] args) {

int[] a = {1, 2, 3, 4, 5, 6};
int[] b = {2, 4, 1, 3, 7, 5};
System.out.println(isSorted(a));
System.out.println(isSorted(b));

}
}
