class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:  
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        DO NOT MODIFY self.
        @return: a ***new*** class Fraction object, which is the sum of self + other.
        '''
        new_numerator = (self.numerator*other.denominator) + (self.denominator*other.numerator)
        new_denominator = (self.denominator*other.denominator)
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: self. The value of self should become the sum of self + other.
        '''
        new_numerator = (self.numerator*other.denominator) + (self.denominator*other.numerator)
        new_denominator = (self.denominator*other.denominator)
        self.numerator = new_numerator
        self.denominator = new_denominator
        return self.numerator/self.denominator

    def __sub__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: a new class Fraction object, which is the subtraction of self - other.
        '''
        new_numerator = (self.numerator*other.denominator) - (self.denominator*other.numerator)
        new_denominator = (self.denominator*other.denominator)
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: a new class Fraction object, which is the multiplication of self * other.
        '''
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.

        If you use the reduce function here, it is fine.

        @return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        '''
        self_fraction = float(self.numerator/self.denominator)
        other_fraction = float(other.numerator/other.denominator)
        if self_fraction == other_fraction:
            return True
        else:
            return False

    
    def reduce(self):
        '''
        Reduces the self Fraction object. 
        Modifies self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        @return: Nothing.
        '''
        if self.numerator > self.denominator:
            small = self.denominator
        else:
            small = self.numerator
            
        for i in range(1, small+1):
            if ((self.numerator%i==0) and (self.denominator%i==0)):
                gcd = i
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)
                
        
    def __str__(self):
        '''
        Displays the self Fraction object nicely. 
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        @return: The string representation of self Fraction object.
        '''
        return str(self.numerator) + " / " + str(self.denominator)

'''
Another note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    x = Fraction(3, 4)
    y = Fraction(4, 6)
    print(x)        # 3 / 4 
    print(y)        # 4 / 6
    print(x + y)    # 34 / 24 or any value that is equal
    z = x + y
    print(x * y)    # 12 / 24 or any value that is equal
    print(x - y)    # 2 / 24 or any value that is equal
    y.reduce()
    print(y)        # 2 / 3
    z.reduce()
    print(z)        # 17 / 12

    print(z == Fraction(-17, -12))  # True
    print(z == Fraction(51, 36))  # True
    print(z == Fraction(-7, 4))   # False

#main()
