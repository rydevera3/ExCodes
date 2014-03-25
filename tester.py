def function1():
    print "Hi. I'm function 1."
def function2():
    print "Hi. I'm function 2."
def function3():
    print "Hi. I'm function 3"
def error_function():
    print "Invalid Option"
    
def test1():
    while 1:
        code = raw_input('Enter "one", "two", "three", or "quit": ')
        
        if code=='quit':
            break
        if code == 'one':
            function1()
        elif code == 'two':
            function2()
        elif code == 'three':
            function3()
        else:
            error_function()
            
def test2():
    mapper = {'one': function1, 'two': function2, 'three': function3}
    while 1:
        code = raw_input('Enter "one", "two", "three", or "quit": ')
        if code == 'quit':
            break
        func = mapper.get(code,error_function)
        func()
        
def test():
    test1()
    print '-' * 50
    test2()
    
if __name__=='__main__':
    test()