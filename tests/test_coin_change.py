from dynamic_programming.coin_change_min_coins import min_coins


def test_coin_change_basic():
    assert min_coins([1, 2, 5], 11) == 3


def test_coin_change_impossible():
    assert min_coins([2], 3) == -1


def test_coin_change_zero():
    assert min_coins([1, 2, 5], 0) == 0
