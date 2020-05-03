# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all the
# numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import basics

def compute(input_list):
    output_list = []
    copy_list = input_list
    for index, value in enumerate(input_list):
        result = 1
        index_number = copy_list[index]
        copy_list[index] = 1
        for x in copy_list:
            result = result * x
        output_list.append(result)
        copy_list[index] = index_number
    return output_list

def main():
    input_list = basics.getNumberList()
    print(compute(input_list))

if __name__ == '__main__':
    main()