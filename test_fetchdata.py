

from fetchdata import Emp
db = None


def setup_module():
    global db;
    db = Emp()
    db.connect('emp.json')


def test_komal_data():
    d = db.retrivedata('komal')
    assert d['eid'] == 1
    assert d['name'] == 'komal'


def test_dhanush_data():
    d = db.retrivedata(('dhanush'))
    assert d['eid'] == 2


def teardown_module():
    print("closed")