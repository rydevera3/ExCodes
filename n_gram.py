# Create an n-grams for tokens

def ngrams(string, N):
    nstring = len(string)
    if N==1 or N>nstring:
        return string
    else:
        NG = []
        for i in range((nstring-N+1)):
            NG.append(string[i:i+N])
            
        NG = sorted(set(NG))
        return NG
        
def test():
    a = 'ryan'
    print ngrams(a,5)
if __name__=='__main__':
    test()
        
        
        
        
        
    
    
    