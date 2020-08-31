# This problem was asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

import basics

def printSubarrayMaxValues(input, k):
    n = len(input)
    if(k<n or k==0):
        print('Invalid value of K..')
    
    kArr = []
    for number in input:
        if(len(kArr)>=k):
            break
        kArr.append(number)

    iterations = n-k
    for i in range(iterations):
        print('Subarray ',i+1,': ',max(kArr))
        kArr.pop(0)
        kArr.append(input[k+i])

    print('Subarray ',n-k+1,': ',max(kArr))


def main():
    input = basics.getNumberList()
    printSubarrayMaxValues(input,3)


if __name__ == '__main__':
    main()