# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

import basics

def first_missing(input_list):
    #create list consisting of only the positive values
    positives = []
    for integer in input_list:
        if integer > 0:
            positives.append(integer) 

    end = len(positives)
    for positive in positives:
        if abs(positive) <= end:
            positives[abs(positive)-1] *= -1

    for i in range(end):
        if positives[i] > 0:
            return i+1
    
    return end + 1

def main():
    assert first_missing([2]) == 1
    assert first_missing([1,2,5]) == 3
    assert first_missing([-1,-2,-3]) == 1
    assert first_missing([1,2]) == 3
    
    print(first_missing(basics.getNumberList()))

if __name__ == '__main__':
    main()