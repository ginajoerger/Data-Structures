def pascal(n):
    '''
    @n: a positive integer.

    @return: a list of sublists. which contains list of pascal values.
    '''
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        newBracket = [1]
        after = pascal(n-1)
        lastOne = after[-1]
        for i in range(len(lastOne)-1):
            newBracket.append(lastOne[i] + lastOne[i+1])
        newBracket += [1]
        after.append(newBracket)
    return after

def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

#main()




