def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return 1 + recur(n // 10)

def iterative(n):
    '''
    Implement this function. This function should do exactly the same job as recur(n).
    '''
    final = 1

    if n < 0:
        return -1

    while n > 10:
        n = n // 10
        final += 1

    return final


def main():
    print(recur(21512))
    print(recur(9891287412))
    print(iterative(21512))
    print(iterative(9891287412))

#main()