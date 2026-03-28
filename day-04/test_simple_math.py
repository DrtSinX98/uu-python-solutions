import simple_math

def test_simple_add():
    assert simple_math.simple_add(2, 3) == 5
    assert simple_math.simple_add(-1, 1) == 0

def test_simple_sub():
    assert simple_math.simple_sub(10, 5) == 5

def test_simple_mult():
    assert simple_math.simple_mult(3, 4) == 12

def test_simple_div():
    assert simple_math.simple_div(10, 2) == 5.0

def test_poly_first():
    # a0 + a1*x  -> 2 + 3*4 = 14
    assert simple_math.poly_first(4, 2, 3) == 14

def test_poly_second():
    # a0 + a1*x + a2*(x**2) -> 1 + 2*3 + 4*(3**2) = 1 + 6 + 36 = 43
    assert simple_math.poly_second(3, 1, 2, 4) == 43