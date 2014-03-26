import numpy as np
import math
import pylab as plt

def UnitCircle(n):
    theta = np.random.randn(1,n)*2*(math.pi)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.figure(0)
    plt.plot(x,y,'bo')
    
    M = np.concatenate((x,y))
    TransformationMatrix = np.random.randn(2,2)
    C = TransformationMatrix.dot(M)
    plt.figure(1)
    plt.plot(C[0],C[1],'r*')
    plt.show()
    
    
def main():
    UnitCircle(1000)
if __name__=='__main__':
    main()

    

    

    
    