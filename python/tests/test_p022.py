from solutions.p022 import solve


def test_colin():
    lst = ["" for i in range(937)]
    lst.append("COLIN")
    assert solve(lst) == 49714
