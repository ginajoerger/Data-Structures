import random


def insertion_sort(array):
    ''' Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. 
        @array: the python list being sorted
    '''
    # To do

    for i in range(1, len(array)): #can exclude first, so 1 to 19 instead of 0 to 19
        number = array[i] #array[1]
        less = i - 1 #0
        while number < array[less] and less >= 0: #while number is less than the one before
            array[less + 1] = array[less] #swap 
            less -= 1 #iterating
        array[less + 1] = number #swap
        
def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    insertion_sort(array)
    print("After sorting:")
    print(array)

#main()