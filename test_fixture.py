

from fetchdata import Emp
import pytest
db = None

@pytest.fixture(scope='module')
def dbcnct():
    print("setup module")
    db=Emp()
    db.connect('emp.json')
    yield
    print("teardown module")


def test_komal_data():
    d = db.retrivedata('komal')
    assert d['eid'] == 1
    assert d['name'] == 'komal'


def test_dhanush_data():
    d = db.retrivedata(('dhanush'))
    assert d['eid'] == 2
