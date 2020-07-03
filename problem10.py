# This problem was asked by Apple.
# Implement a job scheduler which takes in a function 
# f and an integer n, and calls f after n milliseconds.

import time
import threading

#simple version by requirements
def schedule(func, milliseconds):
    time.sleep(milliseconds * 0.001)
    func()

def no_args_function():
    print('Hello, world!')

def main():
    schedule(no_args_function, 5000) 


if __name__ == '__main__':
    main()