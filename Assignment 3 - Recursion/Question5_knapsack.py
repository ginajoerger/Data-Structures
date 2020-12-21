import copy

def knapsack_driver(capacity, weights):
    '''
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information for recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    '''
    figure = []
    ending = []
    location = -1
    
    knapsack(capacity, weights, location, figure, ending)
    
    return ending

def knapsack(capacity, weights, location, figure, ending):
    
    if location == len(weights):
        return
    else: 
        total = 0
        
        for i in figure:
            total = total + i
            
        if capacity == total:
            ending.append(figure)
            return
        
        if location < len(weights) - 1:
            location = location + 1
            newFigures = copy.deepcopy(figure)
            newFigures.append(weights[location])
            knapsack(capacity, weights, location, figure, ending)
            knapsack(capacity, weights, location, newFigures, ending)
        else:
            knapsack(capacity, weights, location+1, figure, ending)

    return ending
    

def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    print(knapsack_driver(14, casts))
#main()

