def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k == 7:
        return True
    if k < 10:
        return False

    def split_nums(k):
        return k//10, k%10

    newnumber, last_digit = split_nums(k)
    if last_digit ==7:
        return True
    return has_seven(newnumber)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"

    def next_num(k, p, up):
        if k == n:
            return p
        if up:
            return switch_dir(k+1, p+1, up)
        else:
            return switch_dir(k+1, p-1, up)

    def switch_dir(k, p, up):
        if k % 7 == 0 or has_seven(k):
            return next_num(k, p, not up)
        else:
            return next_num(k, p, up)

    return next_num(1, 1, True)




