import pytest
from confidential.confidential import Confidential

def test_constructor():
    text1 = 3
    text2 = '£'
    # This is to test that the constructor throws exceptions
    with pytest.raises(Exception):
        assert Confidential(text1) 
        assert Confidential(text2)
    # This is to test the constructor works with spaces
    assert Confidential('ab c') 

def test_convert_text():
    text1 = Confidential('abcd')
    text2 = Confidential('xyz')
    assert text1._convert_text() == [0, 1, 2, 3]
    assert text2._convert_text() == [23, 24, 25]
    
def test_convert_numbers():
    text1 = Confidential('abcdefgh')
    assert text1._convert_numbers([1, 2]) == 'BC'
    assert text1._convert_numbers([25]) == 'Z'
    
def test_parse_keys():
    text1 = Confidential('abcd')
    with pytest.raises(Exception):
        assert text1._parse_keys({}) == {}
        assert text1._parse_keys([]) == {}
        
def test_caesar():
    text1 = Confidential('abc')
    text2 = Confidential('xyz')
    assert text1.caesar(2) == 'CDE'
    
def test_mono():
    text1 = Confidential('abcd')
    assert text1.mono() == []
