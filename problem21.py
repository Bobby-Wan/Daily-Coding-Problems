# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

import basics
import itertools

def needed_rooms(schedule):
    input_data = [' '.join(str(j) for j in i) for i in schedule]
    needed_rooms = 0
    start_times = []
    end_times = []
    for c in schedule:
        start_times.append(c[0])
        end_times.append(c[1])
    start_times.sort()
    end_times.sort()
    
    s = 0
    e = 0
    while(s < len(schedule)):
        if(start_times[s] >= end_times[e]):
            e += 1
        else:
            needed_rooms += 1
        s += 1
    
    return needed_rooms

def main():
    num_of_classes = basics.getNumber()
    schedule = []
    for i in range(num_of_classes):
        interval = basics.getNumberList()
        if(len(interval) > 2):
            raise Exception('Only 2 numbers per interval..')
        schedule.append(interval)
    
    print(needed_rooms(schedule))

if __name__ == '__main__':
    main()

