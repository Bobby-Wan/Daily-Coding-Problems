# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

import basics

def foo(integers, k):
    bag = set()
    for integer in integers:
        if k - integer in bag:
            return True
        else:
            bag.add(integer)
    
    return False

def main():
    
    integers = basics.getNumberList()
    k = basics.getNumber()
    if hasPair(integers, k):
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    main()


    