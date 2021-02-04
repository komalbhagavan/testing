import addsub
import pytest

@pytest.mark.parametrize('a,b,res',[(5,4,9),(10,20,30),('pf','sd','pfsd')])

def test_add(a,b,res):
    assert addsub.add(a,b) == res