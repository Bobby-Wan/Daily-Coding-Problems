# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, 
# and car(pair) and cdr(pair) returns 
# the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, 
# and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

import basics

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def first(a,b):
    return a

def second(a,b):
    return b

def car(pair):
    return pair(first)

def cdr(pair):
    return pair(second)


def main():
    a = basics.getNumber()
    b = basics.getNumber()
    print(car(cons(a,b)))
    print(cdr(cons(a,b)))

if __name__ == '__main__':
    main()