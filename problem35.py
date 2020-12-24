# This problem was asked by Google.
# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. You can only swap 
# elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def make_rgb(array):
    counters = dict()
    counters['R'] = counters['G'] = counters['B'] = 0

    for e in array:
        counters[e] += 1

    current_indexes = dict()
    current_indexes['R'] = 0
    current_indexes['G'] = counters['R']
    current_indexes['B'] = counters['R'] + counters['G']

    for i in range(counters['R']):
        while array[i] != 'R':
            temp = array[i]
            array[i] = array[current_indexes[temp]]
            array[current_indexes[temp]] = temp
            current_indexes[temp] += 1
        current_indexes['R'] += 1
    
    for i in range(current_indexes['G'], counters['R'] + counters['G']):
        while array[i] != 'G':
            temp = array[i]
            array[i] = array[current_indexes[temp]]
            array[current_indexes[temp]] = temp
            current_indexes[temp] += 1

    return array



if __name__ == "__main__":
    assert make_rgb([]) == []
    assert make_rgb(['G','B','R','R','B','R','G']) == ['R','R','R','G','G','B','B']
    assert make_rgb(['B','G','R']) == ['R','G','B']
    