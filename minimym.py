# Author: Ryan de Vera
# Find the minimum value from a list
def minimum(a):
    m = a[0]
    for k in range(len(a)):
        if(a[k]<m):
            m = a[k]
            
    return m
    
def main():
    a = [-2,-11,0,1,7,6]
    print minimum(a)
    
if __name__=='__main__':
    main()

    