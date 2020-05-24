# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def max_sum(list):
    if len(list) == 0:
        return 0
    
    included = list[0]
    excluded = 0

    for i in list[1:]:
        prev_max = max(included, excluded)
        included = excluded + i
        excluded = prev_max
    
    return max(included,excluded)


def main():
    test_arr1 = [5,1,1,5]
    test_arr2 = [2,4,6,2,5]
    print max_sum(test_arr1)
    print max_sum(test_arr2)

if __name__ == '__main__':
    main()