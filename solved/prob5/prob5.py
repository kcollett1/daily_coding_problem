make_list = lambda m,n: [m, n]

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(p):
    return p(make_list)[0]

def cdr(p):
    return p(make_list)[-1]

test = cons(3,4)
print('pair:', test(make_list))
print('first el:', car(test))
print('last el:', cdr(test))
