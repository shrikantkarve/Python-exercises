from dynamic_programming.longest_increasing_subsequence import longest_increasing_subsequence


def _is_subsequence(sub, arr):
    it = iter(arr)
    return all(any(x == y for y in it) for x in sub)


def test_lis_basic():
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    length, seq = longest_increasing_subsequence(arr)
    assert length == 4
    assert len(seq) == 4
    assert all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
    assert _is_subsequence(seq, arr)


def test_lis_empty():
    length, seq = longest_increasing_subsequence([])
    assert length == 0
    assert seq == []


def test_lis_single():
    length, seq = longest_increasing_subsequence([42])
    assert length == 1
    assert seq == [42]
