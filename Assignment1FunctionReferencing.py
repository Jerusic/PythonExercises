from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    return max(a,b)**2 + max(min(a,b), c)**2


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    #This should return anything except 1
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1
    
def f():
    "*** YOUR CODE HERE ***"
    return 0/0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    '''try:
        start = int(n)
    except ValueError:
        print("That's not an int!")
    '''
    assert isinstance(n, int) and n>0, 'n must be an integer and >0'
    i = 1
    print (n)
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        i += 1
        print(n)
    return i

def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x > 0 and y > 0

def falling(n,k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    assert isinstance(n, int) and isinstance(k, int) and n≥k, 'n&k should be ints: n≥k'
    if k == 0: return 1
    else:
        total = 1
        while k≥1:
            total *= n
            n -= 1
            k -=1
    return total

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75


    """
    "*** YOUR CODE HERE ***"
    assert x!=0 and y!=0, 'n&k should be non-zero'
    return (2/((1/x)+(1/y)))

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    if x < power_of_two:        #Option 1 brings power_of_two at or below x if x < 1
        while x < power_of_two:
            power_of_two *= 1/2
    elif x > power_of_two:      #Option 2 brings power_of_two strictly below x if x > 1
        while x > power_of_two:
            power_of_two *= 2
        power_of_two *= 1/2     
    else:
        return power_of_two     #edge case: done only if we start with 1
    #print(power_of_two)             #print test
    if x == power_of_two:        #edge case: done if option 1 made power of 2 equal to x
        return power_of_two 
    elif x == 2*power_of_two:    #edge case: done only if x is a power of 2 (from option 2's loop)
        power_of_two *= 2
    elif x - power_of_two >= 2*power_of_two - x:     #Case: if x is exactly between to power values, or the upper bound is closer, choose upper bound 
        power_of_two *= 2
    return power_of_two
