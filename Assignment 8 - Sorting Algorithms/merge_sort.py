import random

def merge(temp_array1, temp_array2, array):
    """ Merge two sorted lists temp_array1 and temp_array2 into properly sized list S.

        (This is the merge step, merge two sorted lists.)
        
        @temp_array1: left half array copy
        @temp_array2: right half array copy
        @array:       the original array being sorted
    """
    # To do
    while len(array) != 0:
        array.pop()
    
    while len(temp_array1) > 0 and len(temp_array2) > 0:
        if temp_array1[0] < temp_array2[0]:
            new = temp_array1.pop(0)
        else:
            new = temp_array2.pop(0)
        array.append(new)
        
    array += temp_array1 + temp_array2
    
    return array
    

def merge_sort(array):
    """ Sort the elements of Python list using the merge-sort algorithm.
        @array: the original array being sorted
    """
    # To do
    if len(array) < 2:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right, array)

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    merge_sort(array)
    print("After sorting:")
    print(array)

#main()








