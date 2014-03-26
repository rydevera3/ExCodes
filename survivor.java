/*
There are 100 chairs arranged in a circle.
These chairs are numbered sequentially from One to One Hundred.
At some point in time, the person in chair #1 will be 
told to leave the room. The person in chair #2 will 
be skipped, and the person in chair #3 will be told to 
leave. This pattern of skipping one person and telling 
the next to leave will keep going around the circle until 
there is only one person remaining.. the survivor.
Answer: 72
 */

import java.util.ArrayList;

public class Survivor {
    
    public static void main(String[] args){
        System.out.format("The survivor is %d", getChairNumber(100));
    }
    
    private static int getChairNumber(int numChairs){
        if(numChairs<1){
            System.out.println("The number of chairs must be greater than zero");
            return -1;
        }
        
        ArrayList<Integer> chairs = new ArrayList<>();
        for(int k=0;k<numChairs;k++) {
            chairs.add(k+1);
        }
        int idx = 0;
        while(chairs.size()>1) {
            chairs.remove(idx);
            idx++;
            idx %= chairs.size();
                    
                   
        }
        return chairs.get(0);
    }
    
}

