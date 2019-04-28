import pytest
from simplemaths.simplemaths import SimpleMaths as sm

class TestSimpleMaths():
    
    def test_square(self):
        a = sm(3)
        assert a.square() == 9

    def test_factorial(self):
        a = sm(5)
        assert a.factorial() == 120

    def test_constuctor(self):
        a = sm(5)
        assert(a.number == 5)
        
    def test_float(self):
        with pytest.raises(Exception):
            assert sm(2.2)

    def test_string(self):
        with pytest.raises(Exception):
            assert sm('Hello World')

    def test_power(self):
        a = sm(5)
        assert a.power(3) == 125

    def test_square_root(self):
        a = sm(25)
        assert a.square_root() == 5

    def test_even(self):
        a = sm(20)
        assert a.odd_or_even() == 'Even'

    def test_odd(self):
        a = sm(5)
        assert a.odd_or_even() == 'Odd'
        
    def test_neg_even(self):
        a = sm(-2)
        assert a.odd_or_even() == 'Evenx'

    def neg_power(self):
        a = sm(-3)
        assert a.power(3) == -27

    def neg_factorial(self):
        a = sm(-3)
        with pytest.raises(Exception):
            assert a.factorial(-3)
    
    def test_not_square_root(self):
        a = sm(50) 
        assert a.square_root() == pytest.approx(7.071,0.001)
    
    def test_neg_root(self):
        a = sm(-1)
        assert a.square_root() == pytest.approx(1j)
        
    def test_non_int_power(self):
        a = sm(2)
        assert a.power(2.5) == pytest.approx(5.656, 0.001)
    
        
    #### run pytest in terminal 
    
        