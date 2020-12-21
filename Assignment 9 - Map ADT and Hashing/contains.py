def l1_contains_l2(l1, l2):
    ''' checks if every element in l2 exists in l1.
    @l1: the large python list
    @l2: the smaller python list

    Required runtime: Expected O(len(l1) + len(l2))

    return: True if every element in l2 exists in l1. False otherwise.
    '''
    # To do
    main = l1
    new = l2
    final = {}
    final_a = []
    
    for i in range(len(new)):
       if new[i] not in final:
           final[new[i]] = 1
       else:
           final[new[i]] += 1
           
    for i in range(len(main)):
        if main[i] in final:
            final[main[i]] += 1

    final_a = list(final.values())
    
    for i in final_a:
        if i == 1:
            return False

    return True

def main():
    l1 = [1,2,3,4,5,6,7,8,9,0]
    l2 = [5,2,8,9,0,1]
    l3 = [5,2,8,9,0,1,"haha"]
    print("all elements in l2 exists in l1........")
    print("Your result:", l1_contains_l2(l1, l2))
    print("not all elements in l3 exists in l1........")
    print("Your result:", l1_contains_l2(l1, l3))
#main()


