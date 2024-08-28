from sample import myfunc

def test_passed_case():
    assert myfunc(1, 2) == None

def test_failed_case():
    assert myfunc(1, 2) == 2