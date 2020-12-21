def largest_ten(l):
    # Assuming list size greater than 10
    '''
    @l: list of integers
    
    remember to mention your runtime as comment!

    @return: largest ten elements in list l, as a new list. (Order doesn't matter.)
    '''
    top_ten = []

    for i in range(0, 10):
        max_num = 0
    
        for j in range(len(l)):
            if l[j] > max_num:
                max_num = l[j]
    
        l.remove(max_num)
        top_ten.append(max_num)
        
    return(top_ten)

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(largest_ten([9,8,6,4,22,68,96,212,52,12,6,8,99]))

    print(largest_ten([42,10,90,75,79,98,11,90,92,11,21,8,47,72,25,94,99,54,69,60]))

#main()
    
#The worst case runtime for my program is O(n).