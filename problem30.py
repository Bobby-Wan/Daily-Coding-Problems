# This problem was asked by Facebook.
# You are given an array of non-negative integers that represents a 
# two-dimensional elevation map where each element is unit-width wall 
# and the integer is the height. Suppose it will rain and all spots between 
# two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time 
# and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the 
# middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
# 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would 
# run off to the left), so we can trap 8 units of water.

#naive implementation
#does not cover complexity requirements
def rain_water(walls):
    total_water = 0

    for (i,e) in enumerate(walls):
        max_left = 0
        max_right = 0
        for j in range(i):
            if(walls[j] > max_left):
                max_left = walls[j]
        
        for j in range(i+1, len(walls)):
            if(walls[j] > max_right):
                max_right = walls[j]
        
        level = min(max_left, max_right) - walls[i]
        if(level > 0):
            total_water += level

    return total_water

def main():
    print(rain_water([3, 0, 1, 3, 0, 5]))
    print(rain_water([2, 1, 2]))

if __name__ == '__main__':
    main()