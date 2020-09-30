# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and 
# constant space. In other words, find the lowest positive integer that does not exist in 
# the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def first_missing(input):
    length = len(input)
    i = 0
    while(i < length):
        element = input[i]
        if(element <= 0 or element > length or element == i+1 or element == input[element-1]):
            i += 1
        else:
            other_value = input[element-1]
            input[element-1] = element
            input[i] = other_value

    for i in range(length):
        if(input[i] != i+1):
            return i+1
    return length+1

def main():
    assert first_missing([2]) == 1
    assert first_missing([1,2,5]) == 3
    assert first_missing([-1,-2,-3]) == 1
    assert first_missing([1,2]) == 3
    assert first_missing([2,2,1,2,1,3,5]) == 4

if __name__ == '__main__':
    main()