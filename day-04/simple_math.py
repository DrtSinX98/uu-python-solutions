"""
A collection of simple math operations
"""

def simple_add(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    float or int
        The sum of `a` and `b`.
    """
    return a + b

def simple_sub(a, b):
    """
    Subtract the second number from the first.

    Parameters
    ----------
    a : float or int
        The number to be subtracted from.
    b : float or int
        The number to subtract.

    Returns
    -------
    float or int
        The difference between `a` and `b`.
    """
    return a - b

def simple_mult(a, b):
    """
    Multiply two numbers together.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    float or int
        The product of `a` and `b`.
    """
    return a * b

def simple_div(a, b):
    """
    Divide the first number by the second.

    Parameters
    ----------
    a : float or int
        The dividend.
    b : float or int
        The divisor. Must not be zero.

    Returns
    -------
    float
        The quotient of `a` divided by `b`.
    """
    return a / b

def poly_first(x, a0, a1):
    """
    Evaluate a first-degree polynomial.

    Parameters
    ----------
    x : float or int
        The variable to evaluate the polynomial at.
    a0 : float or int
        The constant term (y-intercept).
    a1 : float or int
        The coefficient of the first-degree term.

    Returns
    -------
    float or int
        The result of a0 + a1 * x.
    """
    return a0 + a1 * x

def poly_second(x, a0, a1, a2):
    """
    Evaluate a second-degree polynomial.

    Parameters
    ----------
    x : float or int
        The variable to evaluate the polynomial at.
    a0 : float or int
        The constant term.
    a1 : float or int
        The coefficient of the first-degree term.
    a2 : float or int
        The coefficient of the second-degree term.

    Returns
    -------
    float or int
        The result of a0 + a1 * x + a2 * (x**2).
    """
    return poly_first(x, a0, a1) + a2 * (x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....