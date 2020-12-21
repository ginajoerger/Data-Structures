import random

def selection_sort(array):
    ''' The algorithm proceeds by finding the smallest element in the unsorted sublist, 
        exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
        and moving the sublist boundaries one element to the right. 
        @array: the python list being sorted
    '''
    # Your code
    for i in range(len(array)):
        minimum = min(array[i:])
        minimum_place = array[i:].index(minimum)
        array[i + minimum_place] = array[i] #switch
        array[i] = minimum #finalized switch


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    selection_sort(array)
    print("After sorting:")
    print(array)

#main()