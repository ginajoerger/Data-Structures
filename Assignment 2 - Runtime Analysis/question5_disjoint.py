def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def three_way_disjoint(l1, l2, l3):
    '''
    @l1: first list of elements
    @l2: second list of elements
    @l3: third list of elements

    @return True if l1,l2,l3 are disjoint.
    False if l1,l2,l3 are not disjoint.
    '''
    combined = l1 + l2 + l3
    sorted_list = mergeSort(combined)
        
    a = list(set([x for x in sorted_list if sorted_list.count(x) > 2]))
    
    if len(a) > 0:
        return False
    else:
        return True

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10,11,12]
    l3 = [5,13,14,15,16]
    l4 = [5,6,7,8,9,10,11]

    print(three_way_disjoint(l1,l2,l3))   # True, yes three way disjoint.
    print(three_way_disjoint(l1,l4,l3))   # False, not three way disjoint.
#main()
