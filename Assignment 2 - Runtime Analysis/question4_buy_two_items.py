def buy_two_items(credit, list1):
    '''
    @credit: integer, you want to spend this total amount, exactly.
    @list1: list of integers.

    remember to mention your runtime as comment!

    @return: a tuple of two integers. They should sum up to credit. (Order doesn't matter)
    '''
    second_list = [x for x in list1 if x <= credit]

    for i in second_list:
        del second_list[0]
        for j in second_list:
            if i + j == credit:
                return i, j

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(buy_two_items(200, [150, 24, 79, 50, 88, 345, 3]))  
    print(buy_two_items(295, [678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561]))

#main()
    
#The worst case runtime for my program is O(n^2).