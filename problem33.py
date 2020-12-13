def find_insertion_index(array, element, low, high):
    if len(array) == 0:
        return 0
        
    if high == low:
        if element > array[low]:
            return low+1
        return low

    if element < array[low + int((high-low)/2)]:
        return find_insertion_index(array, element, low,low+int((high-low)/2))
    elif element > array[low + int((high-low)/2)]:
        return find_insertion_index(array,element, low+int((high-low)/2) + 1, high)
    else:
        return int(low+(high-low)/2)
    
def current_median(sequence):
    index_median = 0
    
    sorted = [sequence[0]]
    print(sequence[0])
    for i in range(1, len(sequence)):
        #O(lgn)
        k = find_insertion_index(sorted, sequence[i], 0, len(sorted)-1)
        #O(n), fuck
        sorted.insert(k,sequence[i])
        print('Inserted '+ str(sequence[i])+' at index '+str(k))

        if k > index_median:
            #even index means uneven number of elements
            if i % 2 == 0:
                index_median += 1
                print('Median at index '+ str(index_median))
                print(sorted[index_median]) 
            else:
                print('Median at index '+ str(index_median))
                print((sorted[index_median] + sorted[index_median+1])/2)
        else:
            if i%2==0:
                index_median += 1
                print('Median at index '+ str(index_median))
                print(sorted[index_median])
            else:
                print('Median at index '+ str(index_median))
                print((sorted[index_median] + sorted[index_median+1])/2)

if __name__ == '__main__':
    current_median([2,1,5,7,2,0,5])