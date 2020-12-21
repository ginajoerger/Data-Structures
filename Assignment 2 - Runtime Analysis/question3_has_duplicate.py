def has_duplicate(list1):
    '''
    @l: list of integers

    remember to mention your runtime as comment!

    @return: True if list1 has duplicate, return False otherwise.
    '''
    final_list = []

    for i in range(len(list1)):
        if list1[i] not in final_list:
            final_list.append(list1[i])
        
    if len(list1) != len(final_list):
        return True
    else:
        return False

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

#main()
    
#The worst case runtime for my program is O(n).