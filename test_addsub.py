import addsub
import pytest


@pytest.mark.number


def test_add():
    assert addsub.add(5,4) == 10
    assert addsub.add(6,5) > 10


@pytest.mark.skipif(10 > 5,reason="10 greater than 5")


def test_sub():
    assert addsub.sub(10,5) == 5


@pytest.mark.strings


def test_add_strings():
    c=addsub.add('pf','sd')
    assert c == 'pfsd'
    assert type(c) is str
    print("concacitinated string is",c)


@pytest.mark.parametrize('a,b,res',[(5,4,9),(10,20,40),('pf','sd','pfsd')])