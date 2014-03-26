#Unit Circles based on the p-norm

import pylab as plt
from numpy import array,linalg,random,inf

def plotUnitCircle(p,n):
    for k in range(n):
        x = array([random.randn()*2-1, random.randn()*2-1])
        if linalg.norm(x,p)<1:
            plt.plot(x[0],x[1],'bo')
    plt.axis([-1.5, 1.5, -1.5, 1.5])
        
def main():
    plt.figure(0)
    plotUnitCircle(inf,5000)
    plt.figure(1)
    plotUnitCircle(2,5000)
    plt.show()
if __name__=='__main__':
    main()
        

    

    

    
    