def add(a, b):
    def foo():
        return 'this is local'
    res = foo()
    return res, a + b

def sub(a, b):
    return a - b

if __name__ =="__main__" :
    print(add(5, 2))