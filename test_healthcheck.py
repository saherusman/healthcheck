from healthcheck import get_status


def test_ok():
    assert get_status(50) == "OK"

def test_warn():
    assert get_status(85) == "WARN"

def test_crit():
    assert get_status(95) == "CRIT"

def test_limits():
    assert get_status(79) == "OK"
    assert get_status(80) == "WARN"
    assert get_status(90) == "CRIT"
