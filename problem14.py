# This problem was asked by Google.
# The area of a circle is defined as πr^2. 
# Estimate π to 3 decimal places using a Monte Carlo 
# method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

#working with circle with radius 1
radius = 1

def in_circle(x,y):
    if x * x + y * y < radius:
        return True
    
    return False

#the bigger the range, the more precise the estimate
def circle_total(range_count):
    count = 0
    for i in range(range_count):
        x=random.random()
        y=random.random()
        if in_circle(x,y):
            count+=1
        
    return count/range_count

def main():
    print(circle_total(100000) * 4)

if __name__ == '__main__':
    main()