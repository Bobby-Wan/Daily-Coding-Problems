# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all the
# numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import basics

#O(n) time, O(n) space
def compute(input_list):
    n = len(input_list)
    products = [1 for i in range(n)]
    temp = 1

    for i in range(n):
        products[i] = temp
        temp *= input_list[i]

    temp = 1
    for i in range(n-1, -1, -1):
        products[i] *= temp
        temp *= input_list[i]

    return products

def main():
    assert compute([3,2,1]) == [2,3,6]
    assert compute([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    input_list = basics.getNumberList()
    print(compute(input_list))

if __name__ == '__main__':
    main()