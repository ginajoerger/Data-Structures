import random

def bubble_sort(array):
    ''' Compares each pair of adjacent items and swaps them if they are in the wrong order. 
        @array: the python list being sorted
    '''
    # Your code
    for i in range(len(array) - 1, 0, -1):
        for x in range(i):
            if array[x] > array[x + 1]:
                mat = array[x]
                array[x] = array[x + 1]
                array[x + 1] = mat

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    bubble_sort(array)
    print("After sorting:")
    print(array)

#main()