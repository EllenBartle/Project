import function.calc as fc
import pytest
#import numpy as np
import cmath


def test_positive():
    assert fc.hyp(2,4) > 0, "Squareroot of two positive squared should return a positive."


def test_negative():
    assert fc.hyp(-3,-9) > 0, "Squareroot of two negatives squared should return a positive."


def test_pos_neg():
    assert fc.hyp(-2,10) > 0, "Squareroot of a negative squared and a positive squared should return a positive."


def test_rational():
    assert fc.hyp(7, 2.5) == pytest.approx(7.43, 0.01), "sqrt(7^2 + 2.5^2) should be 7.43."


def test_zero():
    assert fc.hyp(0, 0) == 0,  "Squareroot of zero should return a zero."


def test_imag():
    assert fc.hyp(cmath.complex(3, 1), 2) == cmath.sqrt(cmath.complex (0, 9) + 4), "Squareroot of squareroot of an imaginary number squared, should return an imaginary number "


#def test_inf():
   # assert fc.hyp (np.infty, 3) == np.infty, "Squareroot of infinity squared should return infinity."


