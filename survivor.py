"""
There are 100 chairs arranged in a circle.
These chairs are numbered sequentially from One to One Hundred.
At some point in time, the person in chair #1 will be 
told to leave the room. The person in chair #2 will 
be skipped, and the person in chair #3 will be told to 
leave. This pattern of skipping one person and telling 
the next to leave will keep going around the circle until 
there is only one person remaining.. the survivor.
Answer: 72
"""

import numpy as np

def NumChairs(n):
    if n<=0:
        print("Number of chairs must be greater than zero")
        return
        
    chairs = np.arange(1,n+1)
    s = len(chairs)
    idx = 0
    
    while s>1:
        chairs = np.delete(chairs,idx)
        idx = idx+1
        idx = idx%len(chairs)
        s = len(chairs)
    print("The survivor is chair number " + str(chairs[0]))
    
def main():
    NumChairs(100)
if __name__=='__main__':
    main()
    

