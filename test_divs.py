import divs

def test_div():
    assert divs.div(3, 2) == 1.5
    assert divs.div(4, 2) == 2

def test_div2():
    assert divs.div(14, 3) == 14/3

def test_div_float():
    assert divs.div(14.5, 2) == 7.25

def test_int_divs():
    assert divs.int_div(14, 3) == 5