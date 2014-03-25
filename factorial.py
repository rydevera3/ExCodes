def t(n):
    if n<= 1:
        return n
    else:
        return n*t(n-1)
        
def test():
    numbers = [2,3,4,5]
    factorials = [t(n) for n in numbers]
    print 'factorials: ', factorials
   
if __name__ ==  '__main__':
    test()