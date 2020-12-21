def power(x,n):
    '''
    @x: the base, integer
    @n: the exponent, integer

    x, n can be negative integer.

    @return: x^n
    '''
    if n == 0:
        return 1
    if n >= 1:
        return x * power(x, n-1)
    if n <= -1:
        return (1/power(x, -n))
    

def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125
#main()

